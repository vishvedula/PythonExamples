
#FACEBOOK Hard LEVEL , Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.
#For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

def prepareParentheses(str):
    n = len(str);
    openBrace = closeBrace = 0;
    for x in str:
        if(x=='('):
            openBrace = openBrace+1;
        elif(x == ')'):
            closeBrace = closeBrace +1;
        
    
    #check the counts and prepare the string accordingly
    diff = abs(openBrace - closeBrace);

    if(diff == 0): 
        return;
    elif(diff>0):
        loopValue=int(round(diff+len(str))/2);
        finalStr=''
        for i in range(0,loopValue):
            finalStr = finalStr+'()';
    
    print(finalStr);
    return finalStr;

str = '((((((((())(';
prepareParentheses(str);
