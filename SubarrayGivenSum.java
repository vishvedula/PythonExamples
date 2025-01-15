/*
Subarray with Given Sum
Given a 1-based indexing array arr[] of non-negative integers and an integer sum. You mainly need to return the left and right indexes(1-based indexing) of that subarray. In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

Examples: 

Input: arr[] = [15, 2, 4, 8, 9, 5, 10, 23], target = 23
Output: [2, 5]
Explanation: Sum of subarray arr[2…5] is 2 + 4 + 8 + 9 = 23.


Input: arr[] = [1, 10, 4, 0, 3, 5], target = 7
Output: [3, 5]
Explanation: Sum of subarray arr[3…5] is 4 + 0 + 3 = 7.


Input: arr[] = [1, 4], target = 0
Output: [-1]
Explanation: There is no subarray with 0 sum.
*/

/*Input: arr[] = [15, 2, 4, 8, 9, 5, 10, 23], target = 23
Output: [2, 5]
Explanation: Sum of subarray arr[2…5] is 2 + 4 + 8 + 9 = 23.*/
import java.util.*;
public class findTarget{
  public static void main (String args[]){
    //int x = 23;
    int x = 7;
    //int[] a = {15, 2, 4, 8, 9, 5, 10, 23};
    int[] a = {1, 10, 4, 0, 3, 5};
    
    List<Integer> resultList = findIndexRange(x,a);
    System.out.println(resultList.toString());
  }
  
  public static List<Integer> findIndexRange(int x, int[] a){
    int sum=0;
    List<Integer> list = new ArrayList<Integer>();
    int j=0;
   for(int i=j;i<a.length-1;){
     sum = sum+a[i];
     if(sum<x){
       list.add(i);
        i++;
      continue; 
     } else if(sum==x){
        list.add(i);
       return list;
     } else {
       j=j+1;
       i=j;
       sum=0;
       list.clear();
   }
  }
  return list;
}
}
