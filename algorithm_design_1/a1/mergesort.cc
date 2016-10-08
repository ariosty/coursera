#include <iostream>
using namespace std;

unsigned int merge(int L[], int ll, int R[], int lr, int A[]) {
    int i = 0, j = 0, k = 0, p = 0;
    while (i < ll && j < lr) {
        if (L[i] <= R[j]) {
            A[k++] = L[i++];
        } else {
            A[k++] = R[j++];
            p += ll - i;
        }
    }
    while (i < ll) {
        A[k++] = L[i++];
    }
    while (j < lr) A[k++] = R[j++];
    return p;
}

unsigned int mergeSort(int A[], int n) {
    if (n <= 1) return 0;
    int mid = n / 2;
    int left[mid];
    int right[n - mid];
    for (int i = 0; i < mid; ++i) left[i] = A[i];
    for (int i = mid; i < n; ++i) right[i - mid] = A[i];
    return mergeSort(left, mid) + mergeSort(right, n - mid) + merge(left, mid, right, n - mid, A);
}

int main() {
    const int N = 100000;
    int a[N];
    for (int i = 0; i < N; ++i) cin >> a[i];
    cout << mergeSort(a, N) << endl;
    return 0;
}