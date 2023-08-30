/**Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
*
* You must not use any built-in exponent function or operator.
*
* For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 */


public class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1) {
            return x;
        }
        int minimum = 1;
        int maximum = x;
        int middle = 0;

        while (minimum <= maximum) {
            middle = minimum + (maximum - minimum) / 2;
            int sqrtValue = x / middle;
            if (sqrtValue == middle) {
                return middle;
            } else if (sqrtValue < middle) {
                maximum = middle - 1;
            } else {
                minimum = middle + 1;
            }
        }
        return maximum;
    }
}

   
