import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Created by ji on 10/7/16.
 */
public class Deque<Item> implements Iterable<Item> {

    private int size;
    private Node<Item> first;
    private Node<Item> last;

    public Deque() {
        size = 0;
        first = null;
        last = null;
    }

    public boolean isEmpty() { return (0 == size); }

    public int size() { return size; }

    public void addFirst(Item item) {
        if (null == item)
            throw new NullPointerException("addFirst");

        first = new Node<Item>(item, null, first);
        ++size;
        if (1 == size) last = first;
        if (first.next != null)
            first.next.prev = first;
    }

    public void addLast(Item item) {
        if (null == item)
            throw new NullPointerException("addLast");

        last = new Node<Item>(item, last, null);
        ++size;
        if (1 == size) first = last;
        if (last.prev != null)
            last.prev.next = last;
    }

    public Item removeFirst() {
        if (isEmpty())
            throw new NoSuchElementException("removeFirst");

        final Item retval = first.item;
        first = first.next;
        if (first != null)
            first.prev = null;
        --size;
        if (0 == size) last = null;
        return retval;
    }

    public Item removeLast() {
        if (isEmpty())
            throw new NoSuchElementException("removeLast");

        final Item retval = last.item;
        last = last.prev;
        if (last != null)
            last.next = null;
        --size;
        if (0 == size) first = null;
        return retval;
    }

    @Override
    public Iterator<Item> iterator() {
        return new DequeIterator();
    }

    private class DequeIterator implements Iterator<Item> {
        private Node<Item> current = first;

        @Override
        public boolean hasNext() { return (current != null); }

        @Override
        public void remove() {
            throw new UnsupportedOperationException("remove");
        }

        @Override
        public Item next() {
            if (null == current)
                throw new NoSuchElementException("next");

            final Item retval = current.item;
            current = current.next;
            return retval;
        }
    }

    private static class Node<Item> {
        Item item;
        Node<Item> prev;
        Node<Item> next;

        public Node(Item item, Node<Item> prev, Node<Item> next) {
            this.item = item;
            this.prev = prev;
            this.next = next;
        }
    }
}
