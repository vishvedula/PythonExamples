# 
# This problem was asked by Amazon.
# Given a string s and an integer k, break up the string into multiple texts such that each text has a
# length of k or less. You must break it up so that words don't break across lines. If there's no way to
# break the text up, then return null.
# You can assume that there are no spaces at the ends of the string and that there is exactly one
# space between each word.
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you
# should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a
# length of more than 10.
# 

 
def amazonBreak(str, k):

    strBuff ='';
    finalList =[];
    for i in range(0,len(str)):
        #base condition , to kick out 
            if(len(str[i]) > k):
                print(f'One of the strings is lenghtier than given input string being --> {str[i]} with length {len(str[i])}');
                return None;
            
            if(len(strBuff+str[i]) > k):
                finalList.append(strBuff);
                strBuff = '';
            if(strBuff != ''):
                strBuff = strBuff + ' '+ str[i];
            else:
                strBuff = strBuff + str[i];        
    
    #append the last string to the final result          
    finalList.append(strBuff);       
    print(finalList);
    return finalList;



str = "the quick brown fox jumps over the lazy dog";
str  = str.split(' ');

amazonBreak(str, 10);
