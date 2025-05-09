import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;

/**
 * Problem 1
 * */
interface GeometricObject {
    public double getPerimeter();
    public double getArea();
}

class Circle implements GeometricObject {
    // Protected variable
    /** WRITE YOUR CODE HERE **/

    // Constructor
    /** WRITE YOUR CODE HERE **/
    Circle(double radius){

    }

    // Implement toString method
    public String toString() {
        /**（保留一位小数）
         * output: Circle[radius=2.5]
         * */
        /** WRITE YOUR CODE HERE **/
        return null; // Delete this line
    }

    // Implement methods defined in the interface GeometricObject
    @Override
    public double getPerimeter() {
        /** WRITE YOUR CODE HERE **/
        return 0; // Delete this line
    }
    @Override
    public double getArea() {
        /** WRITE YOUR CODE HERE **/
        return 0; // Delete this line
    }

}

interface Resizable {
    public void resize(int percent);
}

class ResizableCircle extends Circle implements Resizable {
    // Constructor
    /** WRITE YOUR CODE HERE **/
    ResizableCircle(double radius){
        super(radius);
    }

    // Reimplement toString method
    public String toString() {
        /**（保留一位小数）
         * output: ResizableCircle[Circle[radius=2.5]]
         * */
        /** WRITE YOUR CODE HERE **/
        return null;
    }

    // Implement methods defined in the interface Resizable
    @Override
    public void resize(int percent) {
        /** WRITE YOUR CODE HERE **/
    }
}

/**
 * Problem 2
 * */
class MyDate {
    int year;
    int month;
    int day;

    public MyDate(int day, int month, int year) {
        /* WRITE YOUR CODE HERE **/
    }

    public boolean isLeapYear(){
        /* WRITE YOUR CODE HERE **/
        return true; // Delete this line
    }
    public boolean isValidDate(){
        /* WRITE YOUR CODE HERE **/
        return true; // Delete this line
    }
    public void setDate(MyDate date){
        /* WRITE YOUR CODE HERE **/
    }
    public String toStringDate(){
        /* WRITE YOUR CODE HERE **/
        return null; // Delete this line
    }

}

/**
 * Problem 3
 * */
class Trie {
    // add members if you need! you can also define a inner class here
    public boolean search(String s) {
        /** WRITE YOUR CODE HERE **/
        return false; // Delete this line
    }

    public void add(String s) {
        /** WRITE YOUR CODE HERE **/
    }

    public List<String> serialize() {
        /** WRITE YOUR CODE HERE **/
        return null; // Delete this line
    }
}

/**
 * Problem 4
 * */
public class Solution {
    public String executeMethod(Object victim, String methodName) throws Exception {
        Object result = null;
        /* WRITE YOUR CODE HERE **/

        return (String) result;
    }

    public List<String> handleAnimals(Object[] animals, String dogActivity, String catActivity, String wolfRecipe) throws Exception {
        List<String> result = new ArrayList<>();
        /* WRITE YOUR CODE HERE **/

        return result;
    }
}