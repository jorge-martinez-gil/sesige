package lgp;

import com.github.chen0040.gp.lgp.LGP;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;

import com.github.chen0040.data.utils.TupleTwo;
import com.github.chen0040.gp.commons.BasicObservation;
import com.github.chen0040.gp.commons.Observation;
import com.github.chen0040.gp.lgp.gp.Population;
import com.github.chen0040.gp.lgp.program.Program;
import com.github.chen0040.gp.lgp.program.operators.*;
import com.github.chen0040.gp.services.Tutorials;
import com.github.chen0040.gp.utils.CollectionUtils;



public class lgp {
	

	     
	   private static List<Observation> generate2(String file){
		      List<Observation> result = new ArrayList<>();

		        try {
		            final FileInputStream stream = new FileInputStream(file);
					final BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
		            String data = "";
	                data = reader.readLine();
		            do {
		                data = reader.readLine();
		                if (data == null || data.trim().length() == 0) {
		                	continue;
		                } else {
		                	final String [] line = data.split(",");
		                    if (line.length == 6) {
		                        try {
		                            final double a = Double.parseDouble(line[0]);
		                            final double b = Double.parseDouble(line[1]);
		                            final double c = Double.parseDouble(line[2]);
		                            final double d = Double.parseDouble(line[3]);
		                            final double e = Double.parseDouble(line[4]);
		                            final double f = Double.parseDouble(line[5]);
		                            
		        		            Observation observation = new BasicObservation(5, 1);

		        		            observation.setInput(0, b);
		        		            observation.setInput(1, c);
		        		            observation.setInput(2, d);
		        		            observation.setInput(3, e);
		        		            observation.setInput(4, f);

		        		            observation.setOutput(0, a);

		        		            result.add(observation);
		                            
		                                                
		                        } catch(final NumberFormatException e) {
		                            System.out.println(e);
		                        }
		                    }
		                } // End of the if 
		            } while(data != null);            

		            
		        } catch(Exception e) {
		            e.printStackTrace();
		        }
		      return result;
		   } 
	
	   
		public static double getPearson(double[] scores1, double[] scores2) {
			double result = 0;
			double sum_sq_x = 0;
			double sum_sq_y = 0;
			double sum_coproduct = 0;
			double mean_x = scores1[0];
			double mean_y = scores2[0];
			for (int i = 2; i < scores1.length + 1; i += 1) {
				double sweep = Double.valueOf(i - 1) / i;
				double delta_x = scores1[i - 1] - mean_x;
				double delta_y = scores2[i - 1] - mean_y;
				sum_sq_x += delta_x * delta_x * sweep;
				sum_sq_y += delta_y * delta_y * sweep;
				sum_coproduct += delta_x * delta_y * sweep;
				mean_x += delta_x / i;
				mean_y += delta_y / i;
			}
			double pop_sd_x = (double) Math.sqrt(sum_sq_x / scores1.length);
			double pop_sd_y = (double) Math.sqrt(sum_sq_y / scores1.length);
			double cov_x_y = sum_coproduct / scores1.length;
			result = cov_x_y / (pop_sd_x * pop_sd_y);
			
			if (Double.isNaN(result))
				return 0;
			else
				return result;
		}
		
		
		private static double getSpearman(double [] X, double [] Y) {
		       
			try {
			/* Error check */
		        if (X == null || Y == null || X.length != Y.length) {
		            return (Double) null;
		        }
		        
		        /* Create Rank arrays */
		        int [] rankX = getRanks(X);
		        int [] rankY = getRanks(Y);

		        /* Apply Spearman's formula */
		        int n = X.length;
		        double numerator = 0;
		        for (int i = 0; i < n; i++) {
		            numerator += Math.pow((rankX[i] - rankY[i]), 2);
		        }
		        numerator *= 6;
		        return 1 - numerator / (n * ((n * n) - 1));
			}
			catch (Exception e) {
				return -9;
			}
		    }
		    
		    /* Returns a new (parallel) array of ranks. Assumes unique array values */
		    public static int[] getRanks(double [] array) {
		        int n = array.length;
		        
		        /* Create Pair[] and sort by values */
		        Pair [] pair = new Pair[n];
		        for (int i = 0; i < n; i++) {
		            pair[i] = new Pair(i, array[i]);
		        }
		        Arrays.sort(pair, new PairValueComparator());

		        /* Create and return ranks[] */
		        int [] ranks = new int[n];
		        int rank = 1;
		        for (Pair p : pair) {
		            ranks[p.index] = rank++;
		        }
		        return ranks;
		    }
		

	public static void main(String[] args) {
		
		double[] source;
		double[] target;
		
		List<Observation> trainingData = generate2("C:\\geresid-training.txt");
		List<Observation> testingData = generate2("C:\\geresid-validation.txt");
		

		LGP lgp = LGP.defaultConfig();
	      lgp.getOperatorSet().addAll(new Plus(), new Minus(), new Divide(), new Multiply(), new Sine(), new Cosine());
	      lgp.getOperatorSet().addIfLessThanOperator();
	      lgp.addConstants(1.0, 2.0, 3.0, 4.0, 5.0, -1.0, -2.0);
		
		lgp.setRegisterCount(7); // the number of register here is the number of input dimension of the training data times 3
		lgp.setCostEvaluator((program, observations)->{
		 int j = 0;
		 //double error = 0;
		 double[] s = new double [observations.size()];
	     double[] t = new double [observations.size()];
		 for(Observation observation : observations){
		    program.execute(observation);
		    //error += Math.pow(observation.getOutput(0) - observation.getPredictedOutput(0), 2.0);
		    
			 double predicted = observation.getPredictedOutput(0);
			 double actual = observation.getOutput(0);
			 s[j] = predicted;
			 t[j] = actual;
			 j++;
		    
		 }

		 return -getSpearman(s,t);
		});

		lgp.setDisplayEvery(100); // to display iteration results every 10 generation

		Program program = lgp.fit(trainingData);
		System.out.println(program);
		
		int i = 0;
		
		source = new double [testingData.size()];
		target = new double [testingData.size()];
		
		for(Observation observation : testingData) {
			 program.execute(observation);
			 double predicted = observation.getPredictedOutput(0);
			 double actual = observation.getOutput(0);

			 System.out.println (predicted + " " + actual);
			 
			 source[i] = predicted;
			 target[i] = actual;
			 i++;
		}
		
		System.out.println ("Pearson: " + getPearson(target,source));
		System.out.println ("Spearman: " + getSpearman(target,source));
		
		
		
	}

}
