<h1>IntelliQuery</h1>

<p><strong>IntelliQuery</strong> is an AI-driven intelligent search engine designed to provide advanced features such as semantic search, content scraping, similarity search, and customizable filters. Capable of handling up to 1 million results, IntelliQuery also offers real-time data crawling to ensure the most up-to-date search results.</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#features">Features</a></li>
  <li><a href="#requirements">Requirements</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#database-setup">Database Setup</a></li>
  <li><a href="#running-the-project">Running the Project</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="features">Features</h2>
<ul>
  <li><strong>Semantic Search:</strong> Delivers accurate and context-aware search results.</li>
  <li><strong>Content Scraping:</strong> Extracts relevant content from web pages.</li>
  <li><strong>Similarity Search:</strong> Finds similar content across different sources.</li>
  <li><strong>Custom Filters:</strong> Allows powerful search customization.</li>
  <li><strong>High Performance:</strong> Capable of handling up to 1 million results efficiently.</li>
  <li><strong>Up-to-Date Crawling:</strong> Continuously crawls the web to keep data fresh.</li>
</ul>

<h2 id="requirements">Requirements</h2>
<ul>
  <li>Python 3.8 or higher</li>
  <li>Django 5.1</li>
  <li>Exa_py (specific version)</li>
  <li>Other dependencies listed in <code>requirements.txt</code></li>
</ul>

<h2 id="installation">Installation</h2>
<p><strong>Clone the Repository</strong></p>
<pre><code>git clone https://github.com/akhya03/IntelliQuery.git
cd IntelliQuery/searchapp
</code></pre>

<p><strong>Install Dependencies</strong></p>
<p>Before running the project, install the required Python packages:</p>
<pre><code>pip install exa_py
</code></pre>

<h2 id="database-setup">Database Setup</h2>
<p>Run the following commands to set up the database:</p>
<pre><code>python manage.py makemigrations
python manage.py migrate
</code></pre>

<p>Get your API Key from <a href="https://exa.ai">exa.ai</a> and add it to <code>search/views.py</code></p>

<h2 id="running-the-project">Running the Project</h2>
<p>To start the development server, run:</p>
<pre><code>python manage.py runserver
</code></pre>
<p>By default, the application will be available at <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>.</p>

<h2 id="usage">Usage</h2>
<p>After running the server, you can interact with IntelliQuery through the web interface. The main functionalities include:</p>
<ul>
  <li>Entering search queries</li>
  <li>Customizing search filters</li>
  <li>Viewing and analyzing search results</li>
</ul>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to update the documentation if necessary.</p>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more information.</p>
