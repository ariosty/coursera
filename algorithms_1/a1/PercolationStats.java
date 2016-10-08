import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

/**
 * Created by ji on 10/7/16.
 */
public class PercolationStats {

    private final int n;
    private final int trials;
    private final double[] thresholds;

    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0)
            throw new IllegalArgumentException("PercolationStats");

        this.n = n;
        this.trials = trials;
        thresholds = new double[trials];

        for (int i = 0; i < trials; ++i)
            thresholds[i] = trial();
    }

    public double mean() {
        return StdStats.mean(thresholds);
    }

    public double stddev() {
        return StdStats.stddev(thresholds);
    }

    public double confidenceLo() {
        return mean() - 1.96 * stddev() / Math.sqrt(trials);
    }

    public double confidenceHi() {
        return mean() + 1.96 * stddev() / Math.sqrt(trials);
    }

    public static void main(String[] args) {
        final int n = Integer.parseInt(args[0]);
        final int trials = Integer.parseInt(args[1]);
        final PercolationStats ps = new PercolationStats(n, trials);

        StdOut.println("mean                    = " + Double.toString(ps.mean()));
        StdOut.println("stddev                  = " + Double.toString(ps.stddev()));
        StdOut.println("95% confidence interval = " + Double.toString(ps.confidenceLo()) + ", " + Double.toString(ps.confidenceHi()));
    }

    private double trial() {
        final Percolation p = new Percolation(n);
        int picks = 0;
        int i = 0;
        int j = 0;
        while (!p.percolates()) {
            do {
                i = StdRandom.uniform(n) + 1;
                j = StdRandom.uniform(n) + 1;
            } while (p.isOpen(i, j));
            p.open(i, j);
            picks++;
        }
        return picks * 1.0 / n / n;
    }
}
