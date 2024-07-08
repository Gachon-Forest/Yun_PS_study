/*
Date: 2024.07.07
No: 2798
Tier: Bronze 2
Name: 블랙잭
Language: C++
*/

// 뭔 미친 생각으로 이걸 Cpp로 풀었지?


#include<bits/stdc++.h>
using namespace std;
int compare;
int main(){
	int n, m; // 카드의 개수와 Max값
	int temp, temp_sum, arr_end; 
	int arr[100]; //뽑은 카드를 저장하는 배열
	for(int i = 0; i < 100; i++)
		arr[i] = -1; //배열을 -1로 초기화.
	cin >> n >> m;

	/*for(int i = 0; i < 100; i++)
	cout<<arr[i]<<endl;*/

	for(int i = 0; i < n; i++){ //뽑은 카드를 입력하는 부분
		cin >> temp;
		arr[i] = temp;
	}

	for(int i = 0; i < 100; i++){ //배열의 마지막 값을 체크하는 부분.
		//어디까지 입력받을지 몰라서 이렇게 한듯, 걍 뽑은 카드의 수 + 1 크기의 배열 만들면 되는데..
	if(arr[i] == -1){ 
		arr_end = i;
		break;
		}
	}

	int mini = 0;
	//미친듯이 연산.. 해야겠지?
	for(int a = 0; a < arr_end; a++){
		for(int b = 0; b<arr_end; b++){
			for(int c = 0; c < arr_end; c++){
				if(a != b && b != c && a != c){
					temp_sum = arr[a] + arr[b] + arr[c];
					if(temp_sum <= m){
						if((m - mini) > (m - temp_sum))
							mini = temp_sum;
					}
				}
			}
		}
	}
	cout << mini << endl;
	return 0;
}

// 가능하면 파이썬으로 다시 최적화해서 풀어보고 싶음.