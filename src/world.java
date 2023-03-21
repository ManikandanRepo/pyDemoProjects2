public class world extends Hello{
int a = 0;

    public static void main(String[] args){
        Hello.name = "Manikandan Srinivasan";
        System.out.println(Hello.name);
        world w = new world();
        System.out.println(w.city);
        w.test();
        test2();
        //a++;
    }

    public void test(){
        System.out.println(city);
        System.out.println(name);
        test2();
        a++;
    }

    public static void test2(){
        System.out.println("This is inside test2 method");
        world w= new world();
        w.a++;
    }
}
