using System;
using System.Net.Http;
using System.Text;
using System.Xml;
using System.Xml.Serialization;
using System.Xml.Linq;
using Mandatory1.XData;
using System.IO;
using System.Threading.Tasks;

namespace program
{
    class Program
    {
        static void Main(string[] args)
        {
            XData content = new XData(10);
            HttpClient client = new HttpClient();


            // var XMLContent = new XElement("Data",
            // from c in content
            // new XElement("number", c.number));

            
            HttpContent httpContent;
            XmlSerializer serializer = new XmlSerializer(content.GetType());
            using(StringWriter writer = new StringWriter())
            {
                serializer.Serialize(writer, content);
                httpContent = new StringContent(writer.ToString(), Encoding.UTF8, "application/xml");
                Console.WriteLine("####################################################");
                Console.WriteLine(writer.ToString());
            }
            
            Task<HttpResponseMessage> reponse = client.PostAsync("http://127.0.0.1:2222/server1", httpContent);
            Console.WriteLine("#############Content Below#######################");
            Task.WaitAll(reponse);
            
            System.Console.WriteLine(reponse.Result.Content.ReadAsStringAsync().Result);
            
            

            System.Console.WriteLine("#######content above###############");
            System.Console.ReadLine();
        }
    }
}
