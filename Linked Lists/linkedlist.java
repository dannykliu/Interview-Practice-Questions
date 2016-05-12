import java.util.*;

class linkedlist{

	//Trick: Move pointer from longer list ahead by the difference in length
	static Node findIntersection(LinkList a, LinkList b){
		Node currA = a;
		Node currB = b;
		int aLength = 1; //start off at 1 because we're only going until currA.next != null
		int bLength = 1;
		while(currA.next != null){ //retrieve last element
			aLength++;
			currA = currA.next;
		}
		while(currB.next != null){
			bLength++;
			currB = currB.next;
		}
		if(currA != currB) return null; //do not intersect. last nodes are not the same
		currA = a;
		currB = b;
		//now pointer to longer list by difference in length
		//then your collision will be your intersecting node
		//OR you could HashSet all the nodes
		if(aLength > bLength){
			int difference = aLength - bLength;
			for(int i =0; i<difference; i++){
				currA = currA.next;
			}
		} else {
			int difference = bLength - aLength;
			for(int i =0; i<difference; i++){
				currB = currB.next;
			}
		}
		while(currA != currB){
			currA = currA.next;
			currB = currB.next;
		}
		return currA;

	}

	//Trick: Have a runner node going twice as fast 
	static Node detectCircular(LinkList list){
		list.tail.next = list.head; //make list circular to test
		Node slow = list.head;
		Node fast = list.head;
		while(slow != fast){
			if(fast == null || fast.next == null) 
				return null;

			slow = slow.next;
			fast = fast.next.next;
		}
		return fast;
	}

	//Trick: Iterate from end and front of list and check difference count
	static boolean palindrome(LinkList list){
		int different = 0;
		if(list.head == null || list.tail == null){
			return true; //either no elements or 1 element. still a palindrome
		}
		Node tempHead = list.head;
		Node tempTail = list.tail;
		while(tempHead != tempTail){ //if there's an even number of elements, this will iterate through the entire list
			if(!tempHead.name.equals(tempTail.name)){
				different++;
			}
			tempHead = tempHead.next;
			tempTail = tempTail.prev;
			if(different == 2) return false;
		}
		return true;
	}

	//Trick: Keep track of the carry bit of both lists
	//Extended: Set first carry-bit to 0 so that when you add it first time, it does nothing
	static LinkList sumList(LinkList num1, LinkList num2){
		LinkList sum = new LinkList();
		ArrayList<Integer> digits = new ArrayList<Integer>();
		int digit;
		int carry = 0;
		Node num1Head = num1.head;
		Node num2Head = num2.head;
		while(num1Head != null || num2Head!= null){
			if(num1Head != null && num2Head!=null){
				digit = Integer.parseInt(num1Head.name) + Integer.parseInt(num2Head.name) + carry;
				carry = digit/10;	
				digit %=10;		
				digits.add(digit);
				num1Head = num1Head.next;
				num2Head = num2Head.next;	
			} else if(num2Head == null){
				digit = Integer.parseInt(num1Head.name) + carry;
				carry = digit/10;
				digit %=10;
				digits.add(digit);
				num1Head = num1Head.next;
			} else {
				digit = Integer.parseInt(num2Head.name) + carry;
				carry = digit/10;
				digit%=10;
				digits.add(digit);
				num2Head = num2Head.next;
			}
		}
		for(int i = digits.size()-1; i>=0; i--){
			sum.push(""+digits.get(i));
		}
		return sum;
	}

	public static void main(String[] args){
		LinkList myList = new LinkList();
		myList.push("6");
		myList.push("7");
		myList.push("1");
		myList.push("2");
		myList.push("7");
		myList.push("1");
		System.out.println(detectCircular(myList).name);
		LinkList myList2 = new LinkList();
		myList2.push("1");
		myList2.push("2");
		myList2.push("9");
		myList2.push("5");

		//LinkList summedList = sumList(myList, myList2);
		//summedList.loop();
		//myList.removeDuplicatesNoTempBuffer();
		//System.out.println(myList.returnKthToLast(9).name);
		//myList.deleteNode(5);
		//System.out.println(myList.tail.name);
	}
}

class Node{
	Node next;
	Node prev; 
	String name;
	Node(String name){
		this.name = name;
	}
}
//for some functions, we could just create our own LinkList wrapper class around the stdlib LinkList
class LinkList{
	Node head = null; 
	Node tail = null; 

	void setTail(){
		Node curr = head;
		while(curr.next != null){
			curr = curr.next;
		}
		tail = curr; 
	}

	//Trick: Remove nodes then add back
	void partition(int x){
		Node tempHead = head;
		ArrayList<Node> deletedNodes = new ArrayList<Node>();
		int pos = 0;
		while(tempHead != null){
			if(pos == 0){
				deletedNodes.add(pop());
			}else if(Integer.parseInt(tempHead.name) < x){
				deletedNodes.add(tempHead);
				//delete the node now
				if(tempHead.next == null) {
					tempHead.prev.next = tempHead.next;
				} else {
					tempHead.next.prev = tempHead.prev;
					tempHead.prev.next = tempHead.next;
				}
			}
			pos++;
			tempHead = tempHead.next;
		}

		for(int j = deletedNodes.size() -1; j>=0; j--){
			push(deletedNodes.get(j).name);
		}
		setTail();
	}
    
    //deleting first and last nodes require extra care because of nullptrs
    //dangerous, because size of linkedlist now changes. Must be careful with calling deleteNode again
	void deleteNode(int pos){ //solution is trivial bc we have a linkedlist wrapper
		if(pos == 0){
			pop(); //delete from head, what a pain
		} else {
			int i = 0;
			Node temp = head;
			while(temp != null){
				if(i == pos && temp.next == null){ //means we're deleting the last element
					temp.prev.next = temp.next; //delete from tail, what a pain
					tail = temp.prev;
					return;  
				} else if(i == pos){
					temp.prev.next = temp.next;
					temp.next.prev = temp.prev;
					return;
				} else {
					temp = temp.next;
					i++;
				}
			}
			System.out.println("Out of index: " + pos);
		}
	}

	void removeDuplicatesNoTempBuffer(){ //O(1) space, O(n^2) time
		Node temp = head;
		while(temp != null){
			Node temp2 = temp.next;
			while(temp2 != null){
				if(temp.name.equals(temp2.name)){
					Node anotherTemp = temp2;
					removeDoublyLinked(temp2.name);
					temp2 = anotherTemp.next;
				} else {
					temp2 = temp2.next;
				}
			}
			temp = temp.next;
		}
	}

	void removeDuplicates(){ //O(n) space, O(n) time
		Set<String> set = new HashSet<String>();
		Node temp = head; 
		while(temp != null){
			if(set.contains(temp.name)){
				removeDoublyLinked(temp.name);
			} else {
				set.add(temp.name);
			}
			temp = temp.next;
		}
	}

	boolean isEmpty() { return (head == null); } 

	//pushes to head of linked list
	void push(String name){
		Node newNode = new Node(name);
		if(head != null) {
			head.prev = newNode;
		} else {
			tail = newNode; 
		}
		newNode.next = head; //copy ref of the object head to newNode.next
		//note that newNode.prev is still null 
		head = newNode; //copy ref of object newNode to head
	}

	Node pop(){
		Node last = head;
		if(head != null) {
			System.out.println("Item removed: " + head.name);
			head = head.next;
			if(head != null){ 
				head.prev = null;
			} else {
				tail = null; //list is empty
			}
		}
		return last; 
	}

	Node removeDoublyLinked(String name){ 
		if(head.name.equals(name)){
			return pop();
		} else {
			Node temp = head;
			while(temp != null){
				if(temp.name.equals(name)){
					temp.prev.next = temp.next; 
					if(temp.next != null) { //need this because temp.next might be null
						temp.next.prev = temp.prev; //then we'd have a nullptr exception
					} else { 
						tail = temp.prev; //removed the last element. Set tail to prev element
					}
					System.out.println("Item removed: " + temp.name);
					return temp;
				} else{
					temp = temp.next; 
				}

			}
		}
		System.out.println("Item didn't exist");
		return null;
	}

	Node removeSinglyLinked(String name){ 
		if(head.name.equals(name)){
			return pop();
		} else {
			Node prev = head; //prev becomes a reference for head (basically a pointer)
			Node temp = head.next; //temp is a pointer for head.next 
			while(temp != null){
				if(temp.name.equals(name)){
					prev.next = temp.next; 
					System.out.println("Item removed: " + temp.name);
					return temp;
				} else{
					prev = temp; //point prev to temp
					temp = temp.next; //point temp to temp.next
				}

			}
		}
		System.out.println("Item didn't exist");
		return null;
	}

	void loop(){ 
		Node temp = head; 
		while(temp != null){
			System.out.println(temp.name);
			temp = temp.next; //Be careful to not modify temp.next because temp is a pointer!
		}
	}

	Node find(String name){ 
		Node temp = head;
		while(temp != null){
			if(temp.name.equals(name)){
				System.out.println("Found it!");
				return temp;
			} else {
				temp = temp.next;
			}
		}
		System.out.println("Name doesn't exist!"); 
		return null; 
	}
}
