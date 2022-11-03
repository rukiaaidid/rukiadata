def lambda_handler(event, context):
  htmlcode = '''<html>
  <head>
  <title>Climate change: Where we are and what we can do</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
  body {
  background-color: #30412e;
  }
  h1 {
    font-size: 6.25em; /* 100px/16=6.25em */
  }

  h2 {
    font-size: 3.4375em; /* 55px/16=3.4375em */
  }

  h3 {
    font-size: 2.5em; /* 40px/16=2.5em */
  }

    h4 {
    font-size: 2.5em; /* 40px/16=2.5em */
  }

  .container {
    position: relative;
    text-align: center;
    color: white;
    margin:0em;
    padding:0em;
  }
  .climate-change {
    position: absolute;
    top: 20%;
    left: 49%;
    transform: translate(-50%, -40%);
  }
  .where {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -75%);
  }
  * {
    box-sizing: border-box;
  }
  /* Clearfix (clear floats) */
  .row::after {
    content: "";
    clear: both;
    display: table;
  }
  </style>
  <link href="https://fonts.cdnfonts.com/css/gill-sans" rel="stylesheet">
  </head>
  <body>
  <div class="container">
  <img src="https://github.com/HeveB/html/blob/main/Background%203.jpg?raw=true" alt="Forest" style="width:100%;">
  <div class="climate-change"><h1 style="font-family: 'Arial Black', sans-serif;"><b>CLIMATE CHANGE</b></h1></div>
  <div class="where"><h2 style="font-family: 'Arial', sans-serif;font-weight: 700;line-height:1.6em">Where we are and <br> what we can do</h2></div>
  </div>
  
  <hr style= "width:30%;text-align:center; margin-top:3em;">

  <p style="font-family: 'Arial', sans-serif; font-weight:400; font-size:1.125em; line-height:1.9em; color:#ffffff; text-align:left; margin-top:5em; margin-bottom:5em; margin-right:10em; margin-left:10em;">The Intergovernmental Panel on Climate Change (IPCC) has declared that since the start of the Industrial Revolution, humanity has contributed to the continuous release of heat-trapping carbon dioxide into Earth&apos;s atmosphere, eventually causing the air around our planet&apos;s surface to rise by 0.6C on average over the past two decades with most of the heat being absorbed by the oceans.
  <br>
  Through our website we want to present the results of research from the International Energy Agency (IEA) showcasing carbon emissions around the world from 1990 to 2017 and educate readers on the impact this has had on our planet while providing them with a platform to express their own opinions on the topic at hand.
  </p>

  <hr style= "width:30%;text-align:center;"> 

  <p style="font-family: 'Arial', sans-serif; font-weight:700; font-size:2.5em; line-height:1.6em; color:#ffffff; text-align:left; margin-top:2em; margin-bottom:1.875em; margin-right:4.5em; margin-left:4.5em;">Total emissions over time across the World </p>

  <img src="https://github.com/HeveB/html/blob/main/MicrosoftTeams-image%20(2).png?raw=true" alt="World" style="width:40%; display: block;margin-left: auto;margin-right: auto;">

  <p style="font-family: 'Arial', sans-serif; font-weight:400; font-size:1.125em; line-height:1.9em; color:#ffffff; text-align:left; margin-top:2em; margin-bottom:5em; margin-right:10em; margin-left:10em;">This graph shows a significant rise in greenhouse gas emissions from 1990 to 2017. It indicates that Coal, Gas and Oil emissions have increased drastically from 2000 onwards, with approximately a two-fold increase from 2000-2005 compared to 1995-2000.  This is indicative of the increase in human activities undertaken over time which incur emissions.</p>

  <hr style= "width:30%;text-align:center;"> 

  <h3 style="font-family: 'Arial', sans-serif; font-weight:700; line-height:1.6em; color:#ffffff; text-align:left; margin-top:2em; margin-bottom:1.875em; margin-right:2em; margin-left:4.5em;">Coal usage over time across Europe and <br> Asia Pacific </h3>

  <div class="row">
      <div style="float:left; margin-left:11.3em; width: 35%">
      <img src="https://github.com/HeveB/html/blob/main/MicrosoftTeams-image.png?raw=true" alt="World" style="width:86%;">
    </div>
      <div style="float:left; margin-right:10em; width: 35%">
      <img src="https://github.com/HeveB/html/blob/main/MicrosoftTeams-image%20(1).jpg?raw=true" alt="World" style="width:100%;">
    </div>
  </div>

  <p style="font-family: 'Arial', sans-serif; font-weight:400; font-size:1.125em; line-height:1.9em; color:#ffffff; text-align:left; margin-top:2em; margin-bottom:5em; margin-right:10em; margin-left:10em;">The graphs show that there has been a steady downwards trend in the use of coal in Europe from 1990 to 2017, whilst usage has risen significantly in Asia over the same period. This suggests that anthropogenic activities which are energy and resource intensive have moved from Europe towards Asia. These trends support ideas that Globalisation is increasing the flows of trade between Asia and the rest of the world.</p>

  <hr style= "width:30%;text-align:center;">

  <h4 style="font-family: 'Arial', sans-serif; font-weight:700; line-height:1.6em; color:#ffffff; text-align:left; margin-top:2em; margin-bottom:1.875em; margin-right:2em; margin-left:4.5em;">Please answer the following</h4>
  <form style= "margin-left:10em;">
    <label for="email" style="font-family: 'Arial', sans-serif; font-weight:400; line-height:1.6em; color:#ffffff;">Enter your email:</label>
    <input type="email" id="email" name="email" /><br><br>
    <label for="name" style="font-family: 'Arial', sans-serif; font-weight:400; line-height:1.6em; color:#ffffff;">Name:</label>
    <input type="name" id="name" name="user_name" /><br><br>
    <label for="age" style="font-family: 'Arial', sans-serif; font-weight:400; line-height:1.6em; color:#ffffff;">Age:</label>
    <input type="number" id="age" name="age" /><br><br>
    <label for="Q1"style="font-family: 'Arial', sans-serif; font-weight:400; line-height:1.6em; color:#ffffff;" >How do you feel about climate change after viewing our website?</label>
    <input type="name" id="message" name="message"><br><br>
    <input type="reset" value="Reset">
    <input type="submit" value="S
  </form>
  </body>
    </html>'''
  
  response = {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html",},
        'body': htmlcode
    }
    
    return response
  
