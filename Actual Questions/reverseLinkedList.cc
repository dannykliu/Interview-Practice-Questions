#include <iostream>
#include <string>
using namespace std;

//reverse a singly-linked list
struct Node{
	string val;
	Node *next;
};

typedef Node* List;

void reverse(List& first){
	Node *prev = NULL;
	Node *temp = first;
	while(first != NULL){
		temp = first->next; //shift temp
		first->next = prev; //adjust first->next
		prev = first; //shift prev
		first = temp; //shift first
	}
	first = prev;
}

int main (int argc, char* argv[]){
    
}

