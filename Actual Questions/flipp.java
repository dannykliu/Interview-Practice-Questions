import java.util.*;

class flipp{

	static int findMaxProfit(int[] prices){
		int profit = 0;
		int buyPrice = prices[0];
		for(int i =0; i<prices.length; i++){
			if(prices[i] - buyPrice > profit){ //update only when max profit increases 
				profit = prices[i] - buyPrice; //remember the max profit
			}
			if(prices[i] < buyPrice){
				buyPrice = prices[i]; //change buy index if we find a lower profit
			}
		}
		return profit;
	}

	static String largestPermutation(String s){
		int[] freq = new int[128];
		for(int i =0; i<s.length(); i++){
			freq[s.charAt(i) - '0']++; //nth index is now the frequency of the number n 
		}

		String answer = "";
		for(int i = freq.length -1; i>= 0; i--){
			for(int j = 0; j<freq[i]; j++){ 
				answer += i; // works because freq[i] is the amount of times i appears 
			}
		}

		return answer;
	}

	public static void main(String[] args){
		int[] prices = {15, 6, 12, 10, 18, 5, 11};
		String intString = "1334398534096039765";

		System.out.println(largestPermutation(intString));
		System.out.println(findMaxProfit(prices));
	}
}