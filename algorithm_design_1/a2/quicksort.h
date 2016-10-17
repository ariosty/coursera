#ifndef QUICKSORT_H
#define QUICKSORT_H

// different procedures to choose a pivot and swap it with the leftmost element
void choosePivot1(int a[], int left, int right); // a[left]
void choosePivot2(int a[], int left, int right); // a[right]
void choosePivot3(int a[], int left, int right); // median of 3

// partition a[left..right] using a[left] as pivot
int partition(int a[], int left, int right);

// sort a[left..right] using quicksort and add the number of comparisons to *psum
void quicksort(int a[], int left, int right, int &psum);

#endif
