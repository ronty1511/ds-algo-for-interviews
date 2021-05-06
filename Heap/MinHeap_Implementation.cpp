#include <bits/stdc++.h>

using namespace std;

class MinHeap {
  int capacity; //maximum heap capacity
  int sz; //current size of heap, i.e., number of 
          // elements in it
  int *arr; //pointer to heap array

public:
  MinHeap(int capacity) { // (constructor) 
    // initializes variables and heap
    // array. Maximum capacity is set to value
    // passed as parameter
    sz = 0, this->capacity = capacity;
    arr = new int[capacity];
  }

  int parent(int idx) { // Returns index of element's
                        // parent.
    return (idx - 1) / 2;
  }

  void insert(int value) { // inserts value in heap
    if (sz == capacity) {
      cout << "Heap is full." << endl;
      return;
    }

    int idx = ++sz - 1; // Add element at the end of
    arr[idx] = value;   // array and increment size.
    
    // Let the element float up until heap invariant is
    // satisfied.
    while (idx != 0 and arr[parent(idx)] > arr[idx]) {
      swap(arr[parent(idx)], arr[idx]);
      idx = parent(idx);
    }
  }

  void minHeapify(int idx) { // Less prior elements
                             // sink down.

    // Check if the left or right child has higher
    // priority (here, smaller than parent).
    // If so, swap node with the smallest child and
    // do the same for swapped node. Keep doing it,
    // until the parent node is more prior than its
    // children, i.e., heap invariant is satisfied.

    int left = idx * 2 + 1, right = idx * 2 + 2;
    int smallest = idx;

    if (left < sz and arr[left] < arr[smallest])
      smallest = left;
    if (right < sz and arr[right] < arr[smallest])
      smallest = right;

    if (smallest != idx) {
      swap(arr[idx], arr[smallest]);
      minHeapify(smallest);
    }
  }

  int getMin() { // Returns the element at the top
                 // (here, the minimum element).
    return arr[0];
  }

  int pop() { // Removes topmost element and returns it.
    if (sz <= 0)  return INT_MAX;
    if (sz == 1) {
      sz = 0;
      return arr[0];
    }

    int top = arr[0];
    arr[0] = arr[sz-- - 1]; // Put bottom-most and 
                            // right-most value at the 
                            // top and sink it down 
                            // using heapify. Decrement
                            // size since top element has
                            // been removed.
    minHeapify(0);

    return top;
  }

  // This function replaces the value at index idx 
  // with val and if it is lesser than previous value
  // it swims up. THE VALUES PASSED MUST NOT BE GREATER
  // THAN ORIGINAL VALUE.
  void decreaseKey(int idx, int val) {
    arr[idx] = val;

    while (idx != 0 and arr[parent(idx)] > arr[idx]) {
      swap(arr[parent(idx)], arr[idx]);
      idx = parent(idx);
    }
  }
  
  // Replaces the element to be removed by INT_MIN.
  // Now INT_MIN is at the top. It is then extracted from
  // the heap.
  void deleteKey(int idx) {
    decreaseKey(idx, INT_MIN);
    pop();
  }
};

int main() {
  MinHeap h(11);
  h.insert(3);
  h.insert(2);
  h.deleteKey(1);
  h.insert(15);
  h.insert(5);
  h.insert(4);
  h.insert(45);
  cout << h.pop() << endl;
  cout << h.getMin() << endl;
  h.decreaseKey(2, 1);
  cout << h.getMin() << endl;
  return 0;   
}

/*
  Few takeaways after this rigorous implementation are:

  1. A more prior element in the heap should be at the
  top. In case of MinHeap, the most prior element is
  the minimum value, which is opposite in the case of 
  MaxHeap.
  2. While deleting a key, the index of the key needs 
  to be known. Finding this index can lead to O(n) time.
  3. minHeapify(idx) sinks down the node to the desired
  location in order to satisfy heap property also known
  as heap invariant.
  4. priority_queue<int> : MinHeap STL
     priority_queue<int, vector<int>, greater<int>> :
                                            Maxheap STL
  5. MaxHeap can be implemented in a similar fashion. 
*/