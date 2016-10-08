import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

/**
 * Created by ji on 10/8/16.
 */
public class Subset {
    public static void main(String[] args) {
        final int k = Integer.parseInt(args[0]);
        final String[] input = StdIn.readAllStrings();
        final RandomizedQueue<String> rq = new RandomizedQueue<>();
        for (String s : input) {
            rq.enqueue(s);
        }
        for (int i = 0; i < k; ++i) {
            StdOut.println(rq.dequeue());
        }
    }
}
