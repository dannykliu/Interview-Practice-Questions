import java.util.*;

class bazarvoice{

	static String permute(String s, boolean state){
		int freq[] = new int[10];
		for(int i =0; i<s.length(); i++){
			freq[(int)s.charAt(i) - '0']++;
		}
		String myString = "";
		if(state){
			for(int i =0; i<s.length(); i++){
				int key = s.charAt(i) - '0'; //represents the int value of that index
				//freq[key] how many times that key occurs
				if(freq[key] != 0){
					myString += key + "" + freq[key];
					freq[key] = 0;
				}
			}
		} else {
			for(int i =0; i<freq.length; i++){
				if(freq[i] != 0){
					myString += i + "" + freq[i];
				}
			}
		}

		return myString;
	}
	public static void main(String[] args){
		System.out.println(permute("3344445111511233522411", true));
	}
}