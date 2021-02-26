/*
Number of Steps to Reduce a Number to Zero

1st Submission:
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 6 MB, less than 16.47% of C++ online submissions for Number of Steps to Reduce a Number to Zero.
*/
class Solution {
public:
    int numberOfSteps (int num) {
        int counter = 0;
        int steps = num;
        
        for (int i = 0; i < steps; i += 1) {
            if (num % 2 == 1) {
                num = num - 1;
                counter = counter + 1;
            }
            else {
                if (num == 0) {
                    break;
                }
                else {
                    num = num / 2;
                    counter = counter + 1;
                }
            }
        }
        return counter;
    }
};