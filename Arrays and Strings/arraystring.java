import java.util.*;

class arraystring{

	//1.9 O(n) Trick: Append string onto itself
	static boolean stringRotation(String original, String rotated){
		if(original.length() != rotated.length()) return false;
		rotated += rotated;
		if(rotated.indexOf(original) >= 0){
			return true;
		}
		return false;
	}
	//1.8. O(n^2) Jagged matrix. Trick: Use obj to keep track of coordinates. Careful tracking of columns
	static void zeroMatrix(int[][] matrix){
		ArrayList<Coord> myCoord = new ArrayList<Coord>();
		for(int r = 0; r<matrix.length; r++){
			for(int c =0; c<matrix[r].length; c++){
				//System.out.println(matrix[r].length);
				if(matrix[r][c] == 0){
					Coord zero = new Coord(r, c);
					myCoord.add(zero);
				}
			}
		}
		for(int i =0; i<myCoord.size(); i++){
			int zeroRow = myCoord.get(i).row;
			int zeroCol = myCoord.get(i).col;
			for(int c =0; c<matrix[zeroRow].length; c++){
				matrix[zeroRow][c] = 0;
			}
			for(int r = 0; r<matrix.length; r++){
				if(matrix[r].length > zeroCol) //don't set col to 0 if we have a jagged matrix
					matrix[r][zeroCol] = 0;
			}
		}
	}
	//1.7. Trick: Transpose column starts where row begins. int c = r
	static void rotateMatrix(int[][] matrix){
		int n = matrix.length; //number of rows
		//rotate to the right by swapping rows then transposing
		//rotate to the left by transposing then swapping rows 
		//swap rows
		for(int r =0; r<n/2; r++){
			int[] tempRow = matrix[r];
			matrix[r] = matrix[n - r -1];
			matrix[n - r -1] = tempRow;
		}
		//transpose
		for(int r =0; r<n; r++){
			for(int c = r; c<n; c++){
				int temp = matrix[r][c];
				matrix[r][c] = matrix[c][r];
				matrix[c][r] = temp;
			}
		}
	}
	//1.6 O(n). Trick: Add ' ' onto string to check for change and avoid indexOutOfBounds 
	static String compress(String s){
		int inARow = 1;
		String newString = "";
		s += ' '; //trick is to append an extra char onto our string to avoid index out of bounds
		for(int i =0; i<s.length()-1; i++){
			if(s.charAt(i) == s.charAt(i+1)){
				inARow++;
			}else {
				newString += s.charAt(i) + "" + inARow;
				inARow = 1;
			}
		}
		s = s.substring(0, s.length()-1); //chop off our extra appended char
		if(newString.length() < s.length()){
			return newString;
		} else {
			return s;
		}
	}
	//1.5 O(n). Trick: Break into cases and then check for changes in each case
	static boolean oneAway(String original, String changed){
		if(Math.abs(original.length() - changed.length()) > 1) return false;
		if(original.length() == changed.length()){
			int numChanges = 0;
			for(int i =0; i<original.length(); i++){
				if(original.charAt(i) != changed.charAt(i)){
					numChanges++;
				}
				if(numChanges == 2) return false;
			}
		} else if(original.length() - changed.length() == -1){
			int numChanges = 0;
			for(int i =0; i<original.length(); i++){ //iterate through shorter string
				if(original.charAt(i) != changed.charAt(i+numChanges)){ 
					numChanges++;
					i--; //decrement i to reiterate through the loop starting at where the added character occured
				}
				if(numChanges ==2) return false;
			}
		} else if(original.length() - changed.length() == 1){
			int numChanges = 0;
			for(int i =0; i<changed.length(); i++){ //iterate through shorter string
				if(original.charAt(i+numChanges) != changed.charAt(i)){
					numChanges++;
					i--;
				}
				if(numChanges == 2) return false;
			}
		} 
		return true;
	}
	//1.4 O(n). Trick: Palindromes must have one or less singles sandwiched by pairs
	static boolean palindromePermutation(String s){
		int[] frequency = new int[128];
		for(int i =0; i<128; i++){
			frequency[i]=0;
		}
		for(int i =0; i<s.length(); i++){
			if(s.charAt(i) != ' '){
				int asciiValue = (int) s.charAt(i);
				frequency[asciiValue]++;
			}
		}
		int numberOfSingles = 0;
		for(int i =0; i<128; i++){
			if(frequency[i] % 2 != 0){
				numberOfSingles++;
			}
			if(numberOfSingles == 2) return false;
		}
		return true;
	}
	//1.3 O(n). Trick: Modify same string starting from the end and keep track of our space count. Use char array
	//Extra condition: Cannot make new string. Must modify existing string.
	static String urlify(String str, int length){
		char[] s = str.toCharArray();
		int extraSpaces = (s.length - length);
		for(int i = length-1; i>=0; i--){
			if(s[i] == ' '){
				s[i + extraSpaces] = '0';
				s[i + extraSpaces - 1] = '2';
				s[i + extraSpaces -2] ='%';
				extraSpaces -= 2; // -=2 because we've now hit a space and added a new space as extra space
			} else {
				s[i+extraSpaces] = s[i];
			}
		}
		return String.valueOf(s);

	}
	//1.2 O(n). Trick: Use frequency array
	static boolean isPermutation(String s1, String s2){
		if(s1.length() != s2.length()) return false;
		int[] s1frequency = new int[128];
		int[] s2frequency = new int[128];
		for(int i =0; i<s1.length(); i++){
			s1frequency[i] = 0;
			s2frequency[i] = 0;
		}
		for(int i = 0; i<s1.length(); i++){
			int s1key = (int) s1.charAt(i);
			int s2key = (int) s2.charAt(i);
			s1frequency[s1key] = 1;
			s2frequency[s2key] = 1;
		}
		return Arrays.equals(s1frequency, s2frequency);
	}
	//1.1 O(n). Trick: Use frequency array 
	static boolean isUnique(String s){
		int[] frequency = new int[128];
		for(int i =0; i<128; i++){
			frequency[i] = 0;
		}
		for(int i =0; i<s.length(); i++){
			int key = (int) s.charAt(i);
			if(frequency[key] == 0){
				frequency[key] = 1;
			} else {
				return false;
			}
		}
		return true; 
	}

	public static void main(String[] args){
		System.out.println(urlify("Mr John Smith    ", 13));
		System.out.println(palindromePermutation("hello hellod2"));
		System.out.println(oneAway("helflo", "heldlo"));
		System.out.println(compress("aabbccaaa"));
		int[][] matrix = {
							{1, 2, 3, 4}, 
							{5, 6, 7, 8}, 
							{9, 10, 11, 12},
							{13, 14, 15, 16}
						 };
		rotateMatrix(matrix);
		for(int i =0; i<matrix.length; i++){
			for(int k =0; k<matrix.length; k++){
				System.out.print(matrix[i][k] + " ");
			}
			System.out.println();
		}
		System.out.println();
		int[][] matrix2 = {
							{1, 1, 1, 1, 0}, 
							{1, 1, 1, 1}, 
							{1, 1, 1, 1, 1, 1},
							{1, 1, 1, 1}
						 };
		zeroMatrix(matrix2);
		for(int i =0; i<matrix2.length; i++){
			for(int k =0; k<matrix2[i].length; k++){
				System.out.print(matrix2[i][k] + " ");
			}
			System.out.println();
		}

		System.out.println(stringRotation("waterbottle", "erbottlewat"));
		StringBuilder myString = new StringBuilder("hello");
		myString.insert(1, "dick");
		System.out.println(myString.toString());
		myString.delete(2, 5);
		System.out.println(myString);

	}
}
//for 1.8
class Coord{
	int row;
	int col;
	Coord(int row, int col){
		this.row = row;
		this.col = col;
	}
}