import java.util.Scanner;
public class BubbleSortAlgo {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=scanner.nextInt();
        }
        System.out.println();
        System.out.print("Orignal Array ");
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
        for(int i=arr.length-1; i>=0;i--){
            for(int j=0;j<i;j++){
                int left=j;
                int right=j+1;
                if(arr[left]>arr[right]){
                    int temp = arr[left];
                    arr[left] = arr[right];
                    arr[right] = temp;
                }}}
        System.out.println();
        System.out.print("Updated Array ");
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
    }
}
