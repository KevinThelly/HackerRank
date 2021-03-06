#include <bits/stdc++.h>

using namespace std;

// Complete the hourglassSum function below.
int hourglassSum(vector<vector<int>> arr) {
    int k=0;
    int sum[(arr.size()-2)*(arr[0].size()-2)];
    for(int i=0;i<=arr.size()-3;i++){
        for(int j=0;j<=arr[i].size()-3;j++){
            sum[k]=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2] + arr[i+1][j+1];
            k+=1;
        }
    }
    int big=sum[0];
    for(int i=1;i<(arr.size()-2)*(arr[0].size()-2);i++){
        if(sum[i]>big){
            big=sum[i];
        }
    }
    return big;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int i = 0; i < 6; i++) {
        arr[i].resize(6);

        for (int j = 0; j < 6; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = hourglassSum(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
