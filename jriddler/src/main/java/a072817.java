import java.util.*;

public class a072817 {

    public static void dfs(List<Integer> used, List<Integer> longest, int last, Set[] adj) {
        if (used.size() > longest.size()) {
            longest.clear();
            longest.addAll(used);
            System.out.println(longest);
            System.out.println(longest.size());
        }

        Collection<Integer> edges = get_edges(last, adj);
        for (Integer edge : edges) {
            if (!used.contains(edge)) {
                used.add(edge);
                dfs(used, longest, edge, adj);
                used.remove(edge);
            }
        }
    }

    private static Collection<Integer> get_edges(int last, Set<Integer>[] adj) {
        return adj[last];
    }

    public static void main(String[] args) {
        Set[] adj = new Set[101];
        for (int i = 0; i <= 100; i++) {
            adj[i] = new HashSet<Integer>();

        }
        for (int i = 1; i <= 100; i++) {
            int k = 2;
            int t = i * k;
            while (t <= 100) {
                adj[i].add(t);
                adj[t].add(i);
                k++;
                t = i * k;
            }
        }
        List<Integer> used = new ArrayList<>();
        used.add(93);
        List<Integer> longest = new ArrayList<>();
        dfs(used, longest, 93, adj);
    }
}
