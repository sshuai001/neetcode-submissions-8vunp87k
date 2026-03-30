class MinStack {
    //初始化两个数组作为栈与最小栈
    private int[] stack;
    private int[] minStack;
    private int top; 

    public MinStack() {
        stack = new int[100];
        minStack = new int[100];
        top = -1; //代表数组为空
    }
    
    public void push(int val) {
        top++; //top变为0表示第一个可以插入的位置
        stack[top] = val;
        if (top == 0){
            minStack[top] = val;
        }else{
            //top-1指向的是还没有压入元素时上一个状态的最小值
            minStack[top] = Math.min(val,minStack[top - 1]);
        }
    }
    
    public void pop() {
        top--;
    }
    
    public int top() {
        return stack[top];
    }
    
    public int getMin() {
        return minStack[top];
    }
}
