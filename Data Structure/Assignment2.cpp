/* [Question.1] While traversing a single-circular linked list, which condition establishes that the traversing element/variable has reached the first element? */

//[Ans.1]
//Lets take an example and create a basic circular linked list
#include <iostream>
using namespace std;
//Creating List_Node class
class List_Node{
    //Creating class objects
    public:
    int val;
    List_Node*next;
    //Calling List_Node constructor
    List_Node(int val){
        this->val=val;
        next=NULL;
    }
};
//Function to insert a List_node at end on linked list
void add(List_Node*&head,int val){
    List_Node*temp=head;
    List_Node*new_List_node=new List_Node(val);
    if(temp==NULL){head=new_List_node;new_List_node->next=head;return;}
    while(temp->next!=head){temp=temp->next;}   //This condition establishes that the traversing element(temp) has reached the first element
    temp->next=new_List_node;
    new_List_node->next=head;
}
//Function to display elements of linked list from head to the last List_node.
void display(List_Node*&head){
    List_Node*temp=head;
    do{cout<<temp->val<<"->";temp=temp->next;}
    while(temp!=head);
}

int main(){
    List_Node*head=NULL;
    add(head,1);
    add(head,2);
    add(head,3);
    display(head);
}
/*
With reference to above example of circular linked list.

Line 24 i.e. while(temp->next!=head){temp=temp->next;} establishes that the traversing element/variable has reached the first element.

We Know that in circular linked list last List_node of linked list points to head of that linked list, hence we can check if any List_node points to head of linked list then that List_node is the end of circular linked list.
*/


/*[Question.2]  What are the practical applications of a circular linked list? (Try to find applications in your respective fields).

Practical applications of circular linked list are :

1)Multiplayer Games: All the Players are kept in a Circular Linked List and the pointer keeps on moving forward as a player's chance ends.

2)Computing Resources: Circular Linked Lists is used to manage the computing resources of the computer.

3)Fionacci Heap: Circular Linked List is also used in the implementation of advanced val structures such as a Fibonacci Heap.

4)Computer Networking:Circular linked list is also used in computer networking for token scheduling.

5)Implementation of val Structure: val structures such as stacks and queues are implemented with the help of the circular linked lists.

6)Audio/Video Streaming: Circular linked list is also used in audio and video streaming,for ex. when one copmlete audio list finishes playing in music player then it again starts playing from start.

*/


