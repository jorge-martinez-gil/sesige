/*
 * SPDX-FileCopyrightText: 2022 Jorge Martinez Gil <jorgemarcc@gmail.com>
 *
 * SPDX-License-Identifier: MIT
 */

package lgp;
import java.util.Comparator;

/* A class to store 2 variables */
class Pair {
public final int    index;
public final double value;

public Pair(int i, double v) {
    index = i;
    value = v;
}
}

/* This lets us sort Pairs based on their value field */
class PairValueComparator implements Comparator<Pair> {
double epsilon = 0.0001; // shouldn't use " == " to compare "doubles"
@Override
public int compare(Pair p1, Pair p2) {
    if (Math.abs(p1.value - p2.value) < epsilon) {
        return 0;
    } else if (p1.value < p2.value) {
        return -1;
    } else {
        return 1;
    }
}
}