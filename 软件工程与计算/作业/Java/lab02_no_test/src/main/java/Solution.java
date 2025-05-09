import net.sourceforge.pinyin4j.PinyinHelper;
import net.sourceforge.pinyin4j.format.HanyuPinyinCaseType;
import net.sourceforge.pinyin4j.format.HanyuPinyinOutputFormat;
import net.sourceforge.pinyin4j.format.HanyuPinyinToneType;
import net.sourceforge.pinyin4j.format.exception.BadHanyuPinyinOutputFormatCombination;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {

    public void printMatrix(int[][] mat) {
        /**
         * example:
         *  input:
         *      1 2 3 4
         *      10 11 12 5
         *      9 8 7 6
         *  print:
         *      1 2 3 4 5 6 7 8 9 10 11 12
         * **/
        /** WRITE YOUR CODE HERE **/
    }

    public String hex2Bin(String num) {
        /** WRITE YOUR CODE HERE **/
        return null; //Delete this line
    }

    public String strCompression(String str){
        //Returns the compressed string
        /** WRITE YOUR CODE HERE **/
        return null; //Delete this line
    }


    public int strMatching (String str1, String str2){
        //Returns the index
        /** WRITE YOUR CODE HERE **/
        return -1; //Delete this line
    }

    /**
     * Don't change any code about getPinyin function
     * example:
     *  input: '坎'
     *  return: "kan"
     * */
    private String getPinyin(char character){
        String pinyinStr = "";
        HanyuPinyinOutputFormat defaultFormat = new HanyuPinyinOutputFormat();
        defaultFormat.setCaseType(HanyuPinyinCaseType.LOWERCASE);
        defaultFormat.setToneType(HanyuPinyinToneType.WITHOUT_TONE);
        if (character > 128) {
            try {
                String[] strings=PinyinHelper.toHanyuPinyinStringArray(character, defaultFormat);
                if (strings.length==0){
                    return "";
                }
                pinyinStr = strings[0];
            } catch (BadHanyuPinyinOutputFormatCombination e) {
                e.printStackTrace();
            }
        }else{
            return "";
        }
        return pinyinStr;
    }

    public List<String> kyzhyz(List<String> words){
        //Return the Chinese phrase with the format "ky,zhyz" or "kyzhyz" in the input.
        /**
         * input:
         *      {"坎勇，最会游走！","科比，这很硬肘","肉包：狂羊，真狠一撞","狂野震撼亚洲！！","不可以。总会有这样的。"，,"堪忧，最后一"}
         * return:
         *      {"坎勇，最会游走","狂羊，真狠一撞","狂野震撼亚洲"}
         * */
        /** WRITE YOUR CODE HERE **/
        return null; //Delete this line
    }
}
