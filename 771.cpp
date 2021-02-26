/*
Jewels and Stones
1st Submission:
Runtime: 24 ms, faster than 31.56% of Python online submissions for Jewels and Stones.
Memory Usage: 13.4 MB, less than 61.96% of Python online submissions for Jewels and Stones.
*/
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int counter = 0;
        
        for (int i = 0; i < jewels.size(); i += 1) {
            for (int j = 0; j < stones.size(); j += 1) {
                if (stones[j] == jewels[i]) {
                    counter += 1;
                }
            }
        }
        return counter;
    }
};