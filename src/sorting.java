import java.util.*;
import java.util.stream.Collectors;

public class sorting {

        public static void main(String[]args) {


            List<String> names = new ArrayList<String>();

            names.add("Trump");
            names.add("Modi");
            names.add("Abdul");
            names.add("Babu");
            names.add("Balu");
            names.add("Mani");
            names.add("Mankind");
            names.add("Español");
            names.add("Ester");
            names.add("中國人");
            names.add("日本");
            names.add("ชาวไต้หวัน");
            names.add("русский");
            names.add("português");

            Map<String,String> map = new LinkedHashMap<>();
            for (int i=0;i< names.size();i++){
                map.put(String.valueOf(i+1),names.get(i));
            }
            System.out.println(map);
            List<String> mapToListValues = map.values().stream().collect(Collectors.toList());
            System.out.println("Map to list unsorted: "+mapToListValues);
            Collections.sort(mapToListValues);
            System.out.println("Map to list sorted: "+ mapToListValues);
            System.out.println(names);

            Iterator<String> i = names.iterator();
            String current = i.next();
            String previous = i.next();

            while (i.hasNext()) {
                current = i.next();
                if (previous.compareTo(current) > 0) {
                    System.out.println(current + "False");
                }
                previous = current;
            }


            Collections.sort(names);
            System.out.println(names);
            //Iterator<String> j = names.iterator();
            String curr = null;
            String prev = null;
            prev = names.get(0);
            for (int x=0;x<names.size()-1;x++){
                curr = names.get(x+1);
                if (prev.compareTo(curr) > 0) {
                    System.out.println(names.get(x) + "False");
                }
                else{
                    System.out.println(curr + "--True");
                }
                prev = curr;

            }
            /*while (j.hasNext()) {
                curr = j.next();
                if (prev.compareTo(curr) > 0) {
                    System.out.println(j.next() + "False");
                }
                else{
                    System.out.println(prev + "--True");
                }
                prev = curr;
            }*/
            //System.out.println(names);

            names.stream().collect(Collectors.toList());
        }



    }

