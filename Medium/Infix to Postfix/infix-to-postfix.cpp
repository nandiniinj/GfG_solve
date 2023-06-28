//{ Driver Code Starts
// C++ implementation to convert infix expression to postfix
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function to convert an infix expression to a postfix expression.
    
    int precedence(char ch)
    {
        switch (ch) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return -1;
        }
    }
    // int check(char ch)
    // {
    //     if(ch == '+' || ch == '-' || ch == '*' || ch == '/'
    //             || ch == '^') return 1;
    //     else return 0;
    // }
    
    string infixToPostfix(string s) {
        // Your code here
        
        stack<char>stck;
        string postfix;
        
        for (int i=0; i<s.size(); i++){
            char ch=s[i];
            
            if((ch>='a' && ch<='z') || (ch>='A' && ch<='Z') || (ch>='0' && ch<='9')){
                postfix+=ch;
            }
            else if(ch=='('){
                stck.push(ch);
            }
            else if(ch==')'){
                while (!stck.empty() && stck.top()!='('){
                    postfix+=stck.top();
                    stck.pop();
                }
                stck.pop();
            }
            else{
                while(!stck.empty() && precedence(ch)<= precedence(stck.top())){
                    postfix+=stck.top();
                    stck.pop();
                }
                stck.push(ch);
            }
        }
        while(!stck.empty()){
            postfix+=stck.top();
            stck.pop();
        }
        return postfix;
        
        
    }
};


//{ Driver Code Starts.
// Driver program to test above functions
int main() {
    int t;
    cin >> t;
    cin.ignore(INT_MAX, '\n');
    while (t--) {
        string exp;
        cin >> exp;
        Solution ob;
        cout << ob.infixToPostfix(exp) << endl;
    }
    return 0;
}

// } Driver Code Ends