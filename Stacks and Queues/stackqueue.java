import java.util.*;

class stackqueue{

	//Trick: Use a temp variable and a tempStack that's descending(biggest E at top) 
	static void sortStackAscend(Stack<Integer> stack){
		if(stack.size() == 0) return; 

		Stack<Integer> tempStack = new Stack<Integer>();
		int temp;

		while(stack.size() != 0){
			if(tempStack.size() == 0){
				tempStack.push(stack.pop());
			} else if(stack.peek() > tempStack.peek()){
				tempStack.push(stack.pop());
			} else {
				temp = stack.pop(); //pop it off
				while(tempStack.size() != 0 && tempStack.peek() > temp){
					stack.push(tempStack.pop());
				}
				tempStack.push(temp);
			}
		}

		while(tempStack.size() != 0){
			stack.push(tempStack.pop());
		}
	}

	public static void main(String[] args){
		Stack<Integer> myStack = new Stack<Integer>();
		myStack.push(1);
		myStack.push(5);
		myStack.push(2);
		myStack.push(3);
		myStack.push(1);
		//myStack.print();
		sortStackAscend(myStack);
		while(myStack.size() != 0){
			System.out.println(myStack.pop());
		}

	}
}

//Trick: Use a timestamp to check which dog/cat to dequeue
class AnimalShelter2{
	LinkedList<Animal> dogs = new LinkedList<Animal>();
	LinkedList<Animal> cats = new LinkedList<Animal>();
	int time = 0;

	void enqueue(Animal a){
		time++;
		a.time = time;
		if(a.type.equals("dog")){
			dogs.add(a);
		} else if (a.type.equals("cat")){
			cats.add(a);
		} else {
			System.out.println("Not a dog or cat!");
		}
	}
	Animal dequeueAny(){
		if(dogs.peek().time < cats.peek().time){
			dequeueDog();
		} else{
			dequeueCat();
		}
		return null; //will never be reached 
	}
	Animal dequeueDog(){
		if(dogs.size() != 0){
			return dogs.poll(); 
		} 
		return null;
	}
	Animal dequeueCat(){
		if(cats.size() != 0){
			return cats.poll();
		}
		return null;
	}
}

//have to traverse through a linkedlist to remove a specific type of animal
class AnimalShelter{
	LinkedList<Animal> queue = new LinkedList<Animal>();

	void enqueue(Animal animal){
		queue.add(animal);
	}

	Animal dequeueAny(){
		return queue.remove();
	}

	//iterating through a linkedlist...
	Animal dequeueDog(){
		int i =0;
		for(Animal a: queue){
			i++;
			if(a.type.equals("dog")){
				return queue.remove(i);
			}
		}
		return null; //no dog in list
	}
	Animal dequeueCat(){
		for(int i =0; i< queue.size(); i++){
			if(queue.get(i).type.equals("cat")){
				return queue.remove(i);
			}
		}
		return null; //no cat in list
	}

}

class Animal{
	String type;
	int time;
	Animal(String type){
		this.type = type;
	}
}

//Trick: Invert first stack when we need to pop by putting it into the second stack
class QueueAsTwoStacks{
	Stack<Integer> stack = new Stack<Integer>();
	Stack<Integer> queue = new Stack<Integer>();

	void add(int data){
		stack.push(data);
	}

	int remove(){
		if(queue.size() == 0){
			while(stack.size() != 0){
				queue.push(stack.pop());
			}
		}
		return queue.pop();
	}
}

//Trick: Use a stack of stacks. If you need popAt(), use an arraylist of linkedlists
class StackPlates{
	Stack<Stack<Integer>> allPlates = new Stack<Stack<Integer>>();
	int maxHeight;

	StackPlates(int maxHeight){
		this.maxHeight = maxHeight;
	}

	void push(int calories){
		if(allPlates.isEmpty() || allPlates.peek().size() == maxHeight){
			Stack<Integer> newStack = new Stack<Integer>();
			newStack.push(calories);
			allPlates.push(newStack);
		}
		else { //if(allPlates.peek().size() < stackHeight)
			allPlates.peek().push(calories);
		} 
	}

	void print(){ //modifies original stack... be careful
		while(allPlates.size() != 0){
			while(allPlates.peek().size() != 0){
				System.out.println(allPlates.peek().pop());
			}
			allPlates.pop();
		}
	}

	int pop(){
		if(allPlates.isEmpty()){
			throw new EmptyStackException();
		} else if(allPlates.peek().size() > 1){
			//System.out.println("--");
			return allPlates.peek().pop();
		} else {
			int element = allPlates.peek().peek();
			allPlates.pop();
			return element;
		}
	}

	int popAt(int stackNum){
		//popping at a specific stack, we need a list of lists
		//stack of stacks do not seem to work
		//pretending we have an ArrayList of LinkLists...
		//LinkLists are really good because we can always represent a stack or queue with it
		//even the methods are very similar
		//also works with ArrayList of Deques! 
		//this begs the question, LinkList vs Queues to represent stacks/queues?
		// int element = allPlates.get(stackNum).pop();
		// for(int i = stackNum; i<allPlates.size()-1; i++){
		// 	//push onto previous linklist the last element of the next linklist
		// 	allPlates.get(i).push(allPlates.get(i+1).removeLast());
		// }
		// return element;
		return 0;
	}

}

//Trick: Use a second stack to store the past history of all the min values
//Min variable never changes unless we just popped it off our stack
class StackHasMinMethod{
	Stack<Integer> stack = new Stack<Integer>();
	int min = Integer.MAX_VALUE;
	Stack<Integer> minStack = new Stack<Integer>();

	void push(int val){
		if(val<min){
			min = val;
			minStack.push(min);
		}
		stack.push(val);
	}

	int pop(){
		if(!stack.empty()){
			if(stack.peek() == min){
				minStack.pop();
				min = minStack.peek();
			}
			return stack.pop();
		} else {
			throw new EmptyStackException();
		}
	}
	
	int min(){
		if(!stack.empty()){
			return min;
		} else{
			throw new EmptyStackException();
		}
	}
}

//[0, n/3), [n/3, 2n/3), [2n/3, n)
//Trick: Keep track of sizes of each stack with another array 
class ArrayOfNStacks{
	int numStacks = 3; //n
	int stackCapacity;
	int[] values; //store value of all stacks
	int[] sizes = new int[numStacks]; //store size of each individual stack

	ArrayOfNStacks(int stackCapacity){
		values = new int[stackCapacity * numStacks];
		this.stackCapacity = stackCapacity;
	}

	void push(int stackNum, int value){
		if(isFull(stackNum)){
			System.out.println("Sorry, you have reached stack overflow!");
		}
		sizes[stackNum]++;
		values[indexOfTop(stackNum)] = value;
	}

	int peek(int stackNum){
		if(isEmpty(stackNum)){
			throw new EmptyStackException();
		}
		return values[indexOfTop(stackNum)];
	}

	int pop(int stackNum, int value){
		if(!isEmpty(stackNum)){
			int temp = values[indexOfTop(stackNum)];
			values[indexOfTop(stackNum)] = 0;
			sizes[stackNum]--;
			return temp;
		} else {
			throw new EmptyStackException();
		}
	}

	boolean isEmpty(int stackNum){
		return sizes[stackNum] == 0;
	}

	boolean isFull(int stackNum){
		return sizes[stackNum] == stackCapacity;
	}

	int indexOfTop(int stackNum){
		int offset = stackCapacity*stackNum;
		int size = sizes[stackNum];
		return offset + size -1;
	}
}