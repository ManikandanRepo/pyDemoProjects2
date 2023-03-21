import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Hello {

    static String name = "Mani";
    final String city = "Trichy";

    public static void main(String[] args) {
        System.out.println("Hello World!!");
        System.out.println(Hello.name);
        name = "Manikandan";
        System.out.println(Hello.name);


        List<String> ls = new ArrayList<String>();

        ls.add("Manikandan");
        ls.add("Srinivasan");

        ls.forEach(
                (System.out::println)
        );

        System.out.println(ls.stream().filter(e -> e.contains("Mani")).collect(Collectors.toList()));

        String ss = "dasda!@!@!@@#$&^&*^()12122";

        System.out.println(ss.replaceAll("[()]*", ""));

    }

    public void testMethod() {
        System.out.println(Hello.name);
    }
    }


