### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Javascript is a scripting language and python is oop. 
Similar data structures with different names and functionality. 
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
 get("c", "Not Found")
 setdefault('c', 'Not Present')
- What is a unit test?
  Testing one section/function of code. 
- What is an integration test?
  Testing multiple parts of application together
- What is the role of web application framework, like Flask?
  Flask allows python to build web applications. 
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  A URL parameter is best used when you have a general topic about a web page. This will save you time from creating a page for each topic. Instead a page is generated based off a recycled variable. Meanwhile, a query parameter is used when extra personalized information is given. This can come from a user who fills out a form.
- How do you collect data from a URL placeholder parameter using Flask?
  @app.route('/home<id>')  
    def landing_page(id):
- How do you collect data from the query string using Flask?
  request.args('id')
- How do you collect data from the body of the request using Flask?
  request.form.get()
  request.data
- What is a cookie and what kinds of things are they commonly used for?
  A cookie is data stored on the browser as a dictionary. Often used to store users login information. 
- What is the session object in Flask?
  Session is similar to a cookie. Session has a secret key and is also encoded. Session cannot be changed on the clients browser.
- What does Flask's `jsonify()` do?
- returns a string in correct format. 
