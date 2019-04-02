import java.io.*;
import java.lang.reflect.Type;
import java.net.*;
import java.util.*;
import javax.net.ssl.HttpsURLConnection;

/*
 * Gson: https://github.com/google/gson
 * Maven info:
 *    <dependency>
 *      <groupId>com.google.code.gson</groupId>
 *      <artifactId>gson</artifactId>
 *      <version>2.8.1</version>
 *    </dependency>
 */
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.reflect.TypeToken;

/* NOTE: To compile and run this code:
1. Save this file as create_index.java.
2. Run:
	javac create_index.java -cp .;gson-2.8.1.jar -encoding UTF-8
3. Run:
	java -cp .;gson-2.8.1.jar create_index
*/

public class create_index {

// **********************************************
// *** Update or verify the following values. ***
// **********************************************

// Replace this with a valid service name.
	static String service_name = "ENTER SERVICE NAME HERE";

// Replace this with a valid subscription key.
	static String subscriptionKey = "ENTER KEY HERE";

	static String index_name = "test-index";

	static String host = service_name + ".search.windows.net";
	static String operation = "/indexes";
	static String api_version = "2017-11-11";
	static String params = "api-version=" + api_version;

	public static String index = "{" +
    "'name': '" + index_name + "'," +
    "'fields': [" +
        "{ 'name': 'Id', 'type': 'Edm.String', 'key': true, 'searchable': false }," +
        "{ 'name': 'Name', 'type': 'Edm.String', 'searchable': true }" +
    "]" +
	"}";

// This class contains the headers and body of the HTTP response.
	public static class Response {
		int ResponseCode;
		String Response;

		public Response(int response_code, String response) {
			this.ResponseCode = response_code;
			this.Response = response;
		}
	}

	public static URL get_url () throws Exception {
		return new URL ("https://" + host + operation + "?" + params);
	}

	public static String pretty_print (String json_text) {
		JsonParser parser = new JsonParser();
		JsonElement json = parser.parse(json_text);
		Gson gson = new GsonBuilder().setPrettyPrinting().create();
		return gson.toJson(json);
	}

// Send an HTTP POST request.
	public static Response post (URL url, String content) throws Exception {
		HttpsURLConnection connection = (HttpsURLConnection) url.openConnection();
		connection.setRequestMethod("POST");
		connection.setRequestProperty("Content-Type", "application/json");
		connection.setRequestProperty("Content-Length", content.length() + "");
		connection.setRequestProperty("api-key", subscriptionKey);
		connection.setDoOutput(true);

        DataOutputStream wr = new DataOutputStream(connection.getOutputStream());
		byte[] encoded_content = content.getBytes("UTF-8");
		wr.write(encoded_content, 0, encoded_content.length);
		wr.flush();
		wr.close();

		StringBuilder response = new StringBuilder ();
		BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "UTF-8"));
		String line;
		while ((line = in.readLine()) != null) {
			response.append(line);
		}
		in.close();

		return new Response (connection.getResponseCode(), response.toString());
	}

	public static void main(String[] args) {
		try {
			URL url = get_url ();
			System.out.println ("Calling POST " + url.toString() + ".");

			Response response = post(url, index);
			System.out.println ("Status code: " + response.ResponseCode);
			System.out.println (pretty_print (response.Response));
		}
		catch (Exception e) {
			System.out.println (e.toString());
		}
	}
}
