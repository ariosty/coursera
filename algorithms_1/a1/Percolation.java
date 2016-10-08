import edu.princeton.cs.algs4.WeightedQuickUnionUF;

/**
 * Created by ji on 10/7/16.
 */
public class Percolation {

    private final WeightedQuickUnionUF wquf;
    private final int n;
    private final boolean[] isOpened;

    public Percolation(int n) {
        if (n <= 0)
            throw new IllegalArgumentException("non positive grid size");

        this.n = n;
        isOpened = new boolean[n * n];
        for (int i = 0; i < isOpened.length; ++i) isOpened[i] = false;
        wquf = new WeightedQuickUnionUF(n * n + 2);
    }

    public void open(int i, int j) {
        if (i < 1 || i > n || j < 1 || j > n)
            throw new IndexOutOfBoundsException("index out of bound in open");
        isOpened[(i - 1) * n + j - 1] = true;

        // connect with open neighbors
        if (i > 1 && isOpen(i - 1, j))
            wquf.union((i - 1) * n + j, (i - 2) * n + j);
        if (j > 1 && isOpen(i, j - 1))
            wquf.union((i - 1) * n + j, (i - 1) * n + j - 1);
        if (i < n && isOpen(i + 1, j))
            wquf.union((i - 1) * n + j, i * n + j);
        if (j < n && isOpen(i, j + 1))
            wquf.union((i - 1) * n + j, (i - 1) * n + j + 1);

        // connect with top and bottom grids
        if (1 == i)
            wquf.union((i - 1) * n + j, 0);
        if (n == i)
            wquf.union((i - 1) * n + j, n * n + 1);
    }

    public boolean isOpen(int i, int j) {
        if (i < 1 || i > n || j < 1 || j > n)
            throw new IndexOutOfBoundsException("index out of bound in isOpen");
        return isOpened[(i - 1) * n + j - 1];
    }

    public boolean isFull(int i, int j) {
        if (i < 1 || i > n || j < 1 || j > n)
            throw new IndexOutOfBoundsException("index out of bound in isFull");
        return wquf.connected((i - 1) * n + j, 0);
    }

    public boolean percolates() {
        return wquf.connected(0, n * n + 1);
    }
}
