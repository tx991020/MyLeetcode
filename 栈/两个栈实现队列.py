
# 1. Use a second tempStack.
# 2. Pop value from mainStack.
# 3. If the value is greater or equal to the top of tempStack, then push the value in tempStack
# else pop all values from tempStack and push them in mainStack and in the end push value in tempStack
# 4.repeat from step 2 till mainStack is not empty.
# 5. When mainStack will be empty, tempStack will have sorted values in descending order.
# 6. Now transfer values from tempStack to mainStack to make values sorted in ascending order.
'''
def sortStack(stack):

    tempStack = myStack()

    while stack.isEmpty() == False:

        value = stack.pop()

        if value >= tempStack.top():  # if value is larger, it is pushed at the top of tempStack
            tempStack.push(value)
        else:
            while tempStack.isEmpty() == False:
                stack.push(tempStack.pop())
            # place value as the smallest element in tempStack
            tempStack.push(value)

    # Transfer from tempStack => stack
    while tempStack.isEmpty() == False:
        stack.push(tempStack.pop())

    return stack

stack = myStack()
stack.push(2)
stack.push(97)
stack.push(4)
stack.push(42)
stack.push(12)
stack.push(60)
stack.push(23)

sortStack(stack)
sorted = "sorted stack: [ "
for i in range(stack.size()):
    sorted += str(stack.pop()) + " "

sorted += "]"
print sorted

'''


'''
class MyQueue {
    Stack<Integer> temp = new Stack<Integer>();
    Stack<Integer> value = new Stack<Integer>();
 
    // Push element x to the back of queue.
    public void push(int x) {
        if(value.isEmpty()){
            value.push(x);
        }else{
            while(!value.isEmpty()){
                temp.push(value.pop());
            }
 
            value.push(x);
 
            while(!temp.isEmpty()){
                value.push(temp.pop());
            }    
        }
    }
 
    // Removes the element from in front of queue.
    public void pop() {
        value.pop();
    }
 
    // Get the front element.
    public int peek() {
        return value.peek();
    }
 
    // Return whether the queue is empty.
    public boolean empty() {
        return value.isEmpty();
    }
}
'''