//import util.properties packages
import java.util.Properties;

//import simple producer packages
import org.apache.kafka.clients.producer.Producer;

//import KafkaProducer packages
import org.apache.kafka.clients.producer.KafkaProducer;

//import ProducerRecord packages
import org.apache.kafka.clients.producer.ProducerRecord;

import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStream; 
import java.io.InputStreamReader; 
import java.io.OutputStream; 
import java.net.HttpURLConnection; 
import java.net.URL; 
import com.google.gson.Gson;
import java.util.Map;
// import org.json.simple.JSONObject; 
//Create java class named KafkaProducer
public class SimpleProducer {
   
   public static void main(String[] args) throws Exception{
      
      // Check arguments length value
      if(args.length < 2){
         System.out.println("Enter topic name and number of records");
         return;
      }
      while(true){
      try{
        Thread.sleep(1000);    
        URL url = new URL("http://localhost:5000/postjson?count="+args[1].toString());
        HttpURLConnection con = (HttpURLConnection)url.openConnection();
        con.setRequestMethod("POST");
        HttpURLConnection.setFollowRedirects(true);

        con.setDoOutput(true);

        System.out.println("Response Code:" 
                                            + con.getResponseCode()); 
                    System.out.println("Response Message:" 
                                        + con.getResponseMessage()); 
            InputStream ip = con.getInputStream(); 
            BufferedReader br1 =  
                    new BufferedReader(new InputStreamReader(ip)); 

                    StringBuilder response = new StringBuilder(); 
                    String responseSingle = null; 
                    while ((responseSingle = br1.readLine()) != null)  
                    { 
                        response.append(responseSingle); 
                    } 
                    String xx = response.toString();
                    Map<String, Object> map = (Map<String, Object>)new Gson().fromJson(xx, Object.class);
                    // System.out.println("map.get(\"0\") = ");
                    // System.out.println(map.get("0"));
                    // System.out.println("map.get(\"1\") = ");
                    // System.out.println(map.get("1"));
                    // JSONParser parser = new JSONParser();
                    // JSONObject obj = (JSONObject)parser.parse(xx);
                    // // String xx = response.toString().replace(" ", ""); 
                    // System.out.println("This is for 0 : ");
                    
                    // System.out.println((String)obj.get("0"));

                    // System.out.println("This is for 1 : ");
                    // System.out.println((String)obj.get("1"));
                    
                    // // xx=xx.replace(" ", "");
                    // // xx=xx.replace("\t", "");
                //    System.out.println(xx); 
        //Assign topicName to string variable
        String topicName = args[0].toString();
        
        // create instance for properties to access producer configs   
        Properties props = new Properties();
        
        //Assign localhost id
        props.put("bootstrap.servers", "localhost:9092");
        
        //Set acknowledgements for producer requests.      
        props.put("acks", "all");
        
        //If the request fails, the producer can automatically retry,
        props.put("retries", 0);
        
        //Specify buffer size in config
        props.put("batch.size", 16384);
        
        //Reduce the no of requests less than 0   
        props.put("linger.ms", 1);
        
        //The buffer.memory controls the total amount of memory available to the producer for buffering.   
        props.put("buffer.memory", 33554432);
        
        props.put("key.serializer", 
            "org.apache.kafka.common.serialization.StringSerializer");
            
        props.put("value.serializer", 
            "org.apache.kafka.common.serialization.StringSerializer");
        
        Producer<String, String> producer = new KafkaProducer
            <String, String>(props);

        for(Map.Entry<String, Object> entry : map.entrySet())
            producer.send(new ProducerRecord<String, String>(topicName, entry.getKey(), entry.getValue().toString()));   
        //   for(int i = 0; i < 10; i++)
        //      producer.send(new ProducerRecord<String, String>(topicName, 
                // Integer.toString(i), Integer.toString(i)));
                System.out.println("Message sent successfully");
                producer.close();
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
      }

   }
}
