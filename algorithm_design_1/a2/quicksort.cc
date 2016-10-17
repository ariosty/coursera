#include "quicksort.h"
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

void choosePivot1(int a[], int left, int right) {}

void choosePivot2(int a[], int left, int right) {
    swap (a[right], a[left]);
}

void choosePivot3(int a[], int left, int right) {
    int pivot = 0;
    int mid = left + (right - left) / 2;
    if ((a[left] - a[mid]) * (a[left] - a[right]) < 0) {}
    else if ((a[mid] - a[left]) * (a[mid] - a[right]) < 0) {
        swap(a[mid], a[left]);
    }
    else if ((a[right] - a[mid]) * (a[right] - a[left]) < 0) {
        swap(a[right], a[left]);
    }
}

int partition(int a[], int left, int right) {
    int p = a[left];
    int i = left + 1;
    for (int j = left + 1; j <= right; ++j) {
        if (a[j] < p) {
            swap(a[j], a[i]);
            ++i;
        }
    }
    swap(a[left], a[i - 1]);
    return (i - 1);
}

void quicksort(int a[], int left, int right, int &psum) {
    if (left >= right) return;
    psum += (right - left);
    choosePivot3(a, left, right);
    int p = partition(a, left, right);
    quicksort(a, left, p - 1, psum);
    quicksort(a, p + 1, right, psum);
}

int main() {
    int psum = 0;
    int a[10000];
    for (int i = 0; i < 10000; ++i) cin >> a[i];
    quicksort(a, 0, 9999, psum);
    cout << psum << endl;
    return 0;
}