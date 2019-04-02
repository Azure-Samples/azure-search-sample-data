import java.io.*;
import java.lang.reflect.Type;
import java.net.*;
import java.util.*;
import javax.net.ssl.HttpsURLConnection;

/* NOTE: To compile and run this code:
1. Save this file as count_documents.java.
2. Run:
	javac count_documents.java -encoding UTF-8
3. Run:
	java count_documents
*/

public class count_documents {

// **********************************************
// *** Update or verify the following values. ***
// **********************************************

// Replace this with a valid service name.
	static String service_name = "ENTER SERVICE NAME HERE";

// Replace this with a valid subscription key.
	static String subscriptionKey = "ENTER KEY HERE";

	static String index_name = "test-index";

	static String host = service_name + ".search.windows.net";
	static String operation = "/indexes/" + index_name + "/docs/$count";
	static String api_version = "2017-11-11";
	static String params = "api-version=" + api_version;

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

// Send an HTTP GET request.
	public static Response get (URL url) throws Exception {
		HttpsURLConnection connection = (HttpsURLConnection) url.openConnection();
		connection.setRequestMethod("GET");
		connection.setRequestProperty("api-key", subscriptionKey);
		connection.setDoOutput(true);

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
			System.out.println ("Calling GET " + url.toString() + ".");

			Response response = get(url);
			System.out.println ("Status code: " + response.ResponseCode);
			System.out.println ("Document count: " + response.Response);
		}
		catch (Exception e) {
			System.out.println (e.toString());
		}
	}
}
