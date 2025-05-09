import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.*;

/**
 * Problem 1
 * */
class Author {
    /** WRITE YOUR CODE HERE **/
    Author(String name, String email, char gender){

    }
}

class Book {
    /** WRITE YOUR CODE HERE **/
    Book (String name, Author[] authors, double price) {

    }
    Book (String name, Author[] authors, double price, int qty) {

    }

    public String getAuthorNames() {
        return null; //Delete this line
    }
}

/**
 * Problem 2
 * */
class DeathManager{
    public class Person {
        public String name;
        public int health;
        public int strength;
        public int dexterity;
        public int intelligence;
        public int faith;
        public int mana;
        // if you need, you can add other members or methods
        public Person(String name, int health, int strength, int dexterity, int intelligence, int faith, int mana) {
            this.name = name;
            this.health = health;
            this.strength = strength;
            this.dexterity = dexterity;
            this.intelligence = intelligence;
            this.faith = faith;
            this.mana = mana;
            /** WRITE YOUR CODE HERE **/
        }
        public void physicalAttack(Person other){
            /** WRITE YOUR CODE HERE **/
        }
        public void magicAttack(Person other){
            /** WRITE YOUR CODE HERE **/
        }
    }
    public Person newborn(String name,int health, int strength, int dexterity, int intelligence, int faith, int mana){
        return new Person(name, health, strength, dexterity, intelligence, faith, mana);//Do not modify
    }
    public void progressYear() {
        /** WRITE YOUR CODE HERE **/
    }
    public Map<String, Integer> deathRecord() {
        /** WRITE YOUR CODE HERE **/
        return null;//Delete this line
    }

    /**
     * Problem 3
     * */
    public void grantItem(Person person, Item item) {
        /** WRITE YOUR CODE HERE **/
    }

    public void removeItem(Person person, Item item) {
        /** WRITE YOUR CODE HERE **/
    }

    private static class Item {
        void activeSkill(Person other) {
        }
    }

    public static class Blade extends Item {
        /** WRITE YOUR CODE HERE **/
    }

    public static class Shield extends Item {
        /** WRITE YOUR CODE HERE **/
    }

    public static class Wand extends Item {
        /** WRITE YOUR CODE HERE **/
    }

    public static class RingOfSacrifice extends Item {
        /** WRITE YOUR CODE HERE **/
    }

    public static class CalamityRing extends Item {
        /** WRITE YOUR CODE HERE **/
    }

    public static class RingOfTheEvilEye extends Item {
        /** WRITE YOUR CODE HERE **/
    }
}

/**
 * Problem 4
 * */
public class Solution {
    public boolean checkClassInfo(String path) {
        try {
            /** WRITE YOUR CODE HERE **/
            Class<?> c = Class.forName(path);
        }
        catch (ClassNotFoundException ignored) {
            return false; // error handling, simply returns false
        }
        return false;
    }
}
