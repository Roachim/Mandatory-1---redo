using System;
using System.Net.Http;
using System.Text;
using System.Xml;
using System.Xml.Serialization;

namespace Mandatory1.XData
{
    [Serializable]
    public class XData
    {
        public int Number { get; set; }

        public XData(int number){
            Number = number;
        }
        public XData()
        {
            
        }
    }
}