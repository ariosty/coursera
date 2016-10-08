import java.util.Iterator;
import java.util.NoSuchElementException;

import edu.princeton.cs.algs4.StdRandom;

/**
 * Created by ji on 10/8/16.
 */
public class RandomizedQueue<Item> implements Iterable<Item> {

    private Item[] data;
    private int size;
    private int capacity;

    @SuppressWarnings("unchecked")
    public RandomizedQueue() {
        capacity = 8;
        data = (Item[]) new Object[capacity];
        size = 0;
    }

    public boolean isEmpty() { return (0 == size); }

    public int size() { return size; }

    @SuppressWarnings("unchecked")
    public void enqueue(Item item) {
        if (null == item)
            throw new NullPointerException("enqueue");

        data[size] = item;
        ++size;
        resize();
    }

    public Item dequeue() {
        if (isEmpty())
            throw new NoSuchElementException("dequeue");

        final int index = StdRandom.uniform(size);
        Item temp = data[size - 1];
        data[size - 1] = data[index];
        data[index] = temp;
        final Item retval = data[size - 1];
        --size;
        data[size] = null;
        resize();
        return retval;
    }

    public Item sample() {
        if (isEmpty())
            throw new NoSuchElementException("sample");

        return data[StdRandom.uniform(size)];
    }

    @Override
    public Iterator<Item> iterator() {
        return new QueueIterator();
    }

    @SuppressWarnings("unchecked")
    private void resize() {
        int newCapacity = capacity;
        if (size == capacity) {
            newCapacity *= 2;
        } else if (capacity > 8 && size <= capacity / 4) {
            newCapacity /= 2;
        }
        if (newCapacity != capacity) {
            capacity = newCapacity;
            Item[] newData = (Item[]) new Object[capacity];
            for (int i = 0; i < size; ++i) newData[i] = data[i];
            data = newData;
        }
    }

    private class QueueIterator implements Iterator<Item> {
        private final int[] order;
        private int current;

        public QueueIterator() {
            order = new int[size];
            for (int i = 0; i < order.length; ++i) order[i] = i;
            StdRandom.shuffle(order);
            current = 0;
        }

        @Override
        public boolean hasNext() { return (current < size); }

        @Override
        public Item next() {
            if (!hasNext())
                throw new NoSuchElementException("next");

            final Item retval = data[order[current]];
            ++current;
            return retval;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException("remove");
        }
    }
}
