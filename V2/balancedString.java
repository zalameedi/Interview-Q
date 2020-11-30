class Solution {
    public int balancedStringSplit(String s) {
        int count_R = 0;
        int count_L = 0;
        int RL_pairs = 0;
        
        for(char x : s.toCharArray())
        {
            if (x == 'R')
                count_R += 1;
            else
                count_L += 1;
            if(count_R == count_L)
                RL_pairs += 1;
        }
        return RL_pairs;
    }
}