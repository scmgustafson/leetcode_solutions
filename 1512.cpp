/* 
Number of Good Pairs

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Good Pairs.
Memory Usage: 7.2 MB, less than 93.02% of C++ online submissions for Number of Good Pairs.
*/

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int good_pairs = 0;
        for (int i = 0; i < nums.size(); i += 1) {
            for (int j = 0; j < nums.size(); j += 1) {
                if ((nums[i] == nums[j]) and (i < j)) {
                    good_pairs += 1;
                }
            }
        }
        return good_pairs;
    }
};