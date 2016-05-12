import java.util.*;

class linkedlist{

	public static void main(String[] args){
		LinkList myList = new LinkList();
		myList.push("Danny");
		myList.pop();
		//System.out.println(myList.tail.name);
	}
}

//if we have a doubly-linked list, just change the mutator methods (push, pop, remove)
//This is our ultimate linked list: a double ended doubly-linked list
class Node{
	Node next;
	Node prev; //doubly-linked list
	String name;
	Node(String name){
		this.name = name;
	}
}
class LinkList{
	Node head = null; //our LinkList only has reference to this node. it starts off as null
	Node tail = null; //jk it had a reference to this guy too
	//With a double ended linked list, don't worry about tail unless the last element has been changed
	boolean isEmpty() { return (head == null); } //if head is null, our list is empty

	void push(String name){
		Node newNode = new Node(name);
		if(head != null) {
			head.prev = newNode;
		} else {
			tail = newNode; //if head is null, then the tail will be our first node
		}
		newNode.next = head; //copy ref of the object head to newNode.next
		//note that newNode.prev is still null and ALWAYS will be until another Node is pushed
		/*
			When you do object assignment in Java, a ref pointer (which is a value) is created 
			and points to the same object as the object on the right of the equals sign.
			(Somehow this pointer is a copy of the object and is huge, but we can forget about that)
		*/
		head = newNode; //head now points to the new node. When you append again, head will be the preivous node
	}

	Node pop(){
		Node last = head;
		if(head != null) {
			head = head.next;
			if(head != null){ //this means head is the last element
				head.prev = null;
			} else {
				tail = null; //therefore change tail to point to null 
			}
		}
		System.out.println("Item removed succesfully");
		return last; //will be null if the list is empty 
	}

	Node removeDoublyLinked(String name){ //keeps track of head, tail, prev, and next
		if(head.name.equals(name)){
			return pop();
		} else {
			Node temp = head;
			while(temp != null){
				if(temp.name.equals(name)){
					temp.prev.next = temp.next; 
					if(temp.next != null) { //need this in case we're deleting the first element.
						temp.next.prev = temp.prev; //otherwise we get a nullpointer exception here
					} else { //cannot assign something to a nullptr
						tail = temp.prev; // need this because we removed the last element
					}
					System.out.println("Item removed succesfully");
					return temp;
				} else{
					temp = temp.next; //point temp to temp.next
				}

			}
		}
		System.out.println("Item didn't exist");
		return null;
	}

	Node remove(String name){ //just keeps track of head
		if(head.name.equals(name)){
			return pop();
		} else {
			Node prev = head; //prev becomes a reference for head (basically a pointer)
			Node temp = head.next; //temp is a pointer for head.next 
			while(temp != null){
				if(temp.name.equals(name)){
					prev.next = temp.next; 
					System.out.println("Item removed succesfully");
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

	void loop(){ //not a mutator method! Therefore must use temp to cycle through!
		Node temp = head; //need temp variable because we want to keep the reference to the head 
		while(temp != null){
			System.out.println(temp.name);
			temp = temp.next; //point temp to temp.next. Be careful to not modify temp.next because temp is a pointer!
		}
	}

	Node find(String name){ //also not a mutator method. therefore must need temp
		Node temp = head;
		while(temp != null){
			if(temp.name.equals(name)){
				System.out.println("Found it!");
				return temp;
			} else {
				temp = temp.next;
			}
		}
		System.out.println("Name doesn't exist!"); //by the time we're here, the name has not been found
		return null; //will be null because we're done traversing the list 
	}
}