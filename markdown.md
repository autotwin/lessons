# Start Using Markdown (Stop Using Word)

## Problems with Word

* The file is serialized in a binary format that can only be viewed and decoded with the Word application.
* The Word application is proprietary, closed-source, and costs money.
* The file is not suited for diffing via source control.
* Sharing and collaborating is difficult, and typically involves emailing a file back and forth.

## Benefits of Word

* Track changes, but version-itis can clobber and confound this benefit.
* Grammar check
* Spell check

## Benefits of Markdown

* The file is serialzed in a text format that can be viewed by any text editor.
* There is no mandatory application that must be used to view Markdown.
* Markdown is not proprietary, and costs nothing.
* The file is extremely well suited for diffing via source control.
* Sharing and collaborating is easy, and favors source control, avoiding emailing files back and forth.
* Track changes is implicit when used on a repository.

## Limitations of Markdown

* Grammar check nonexistent
* Spell check nonexistent

## Cheat Sheet

To get started, reivew the [Markdown Guide](https://www.markdownguide.org/).

Below the [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) is restated as a version local to this repository.

This Markdown cheat sheet provides a quick overview of all the Markdown syntax elements. It can’t cover every edge case, so if you need more information about any of these elements, refer to the reference guides for [basic syntax](https://www.markdownguide.org/basic-syntax) and [extended syntax](https://www.markdownguide.org/extended-syntax).

## Basic Syntax

These are the elements outlined in John Gruber’s original design document. All Markdown applications support these elements.

Element | Markdown Syntax | Rendered Output
-- | -- | --
[Heading](https://www.markdownguide.org/basic-syntax/#headings) | `# Heading 1`</br>`## Heading 2`</br>`### Heading 3` | <h1>Heading 1</h1></br><h2>Heading 2</h2></br><h3>Heading 3</h3>
[Bold](https://www.markdownguide.org/basic-syntax/#bold) | `**bold text**` | **bold text**
[Italic](https://www.markdownguide.org/basic-syntax/#italic) | `*italicized text*` | *italicized text*
[Blockquote](https://www.markdownguide.org/basic-syntax/#blockquotes-1) | `> blockquote` | > blockquote
[Ordered List](https://www.markdownguide.org/basic-syntax/#ordered-lists) | `1. First item`</br>`2. Second item`</br>`3. Third item` | 1. First item</br>2. Second item</br>3. Third item
[Unordered List](https://www.markdownguide.org/basic-syntax/#unordered-lists) | `- First item`</br>`- Second item`</br>`- Third item` | <li>First item</li><li>Second item</li><li>Third item</li>
[Code](https://www.markdownguide.org/basic-syntax/#code) | `code`
[Horizontal Rule](https://www.markdownguide.org/basic-syntax/#horizontal-rules) | --- |
[Link](https://www.markdownguide.org/basic-syntax/#links) | `[title](https://www.github.com)` | [GitHub](https://www.github.com)
[Image](https://www.markdownguide.org/basic-syntax/#images-1) | `![alt text](https://www.markdownguide.org/assets/images/tux.png)` | ![tux](https://www.markdownguide.org/assets/images/tux.png)</br>

## Extended Syntax

These elements extend the basic syntax by adding additional features. Not all Markdown applications support these elements.

<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th>Element</th>
      <th>Markdown Syntax</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#tables">Table</a></td>
      <td><code>
          | Syntax      | Description |<br>
          | ----------- | ----------- |<br>
          | Header      | Title       |<br>
          | Paragraph   | Text        |
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#fenced-code-blocks">Fenced Code Block</a></td>
      <td><code>```<br>
      {<br>
      &nbsp;&nbsp;"firstName": "John",<br>
      &nbsp;&nbsp;"lastName": "Smith",<br>
      &nbsp;&nbsp;"age": 25<br>
      }<br>
      ```
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#footnotes">Footnote</a></td>
      <td><code>
        Here's a sentence with a footnote. [^1]<br><br>
        [^1]: This is the footnote.
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#heading-ids">Heading ID</a></td>
      <td><code>### My Great Heading {#custom-id}</code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#definition-lists">Definition List</a></td>
      <td><code>
        term<br>
        : definition
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#strikethrough">Strikethrough</a></td>
      <td><code>~~The world is flat.~~</code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#task-lists">Task List</a></td>
      <td><code>
        - [x] Write the press release<br>
        - [ ] Update the website<br>
        - [ ] Contact the media
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#emoji">Emoji</a><br>(see also <a href="https://www.markdownguide.org/extended-syntax/#copying-and-pasting-emoji">Copying and Pasting Emoji</a>)</td>
      <td><code>
        That is so funny! :joy:
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#highlight">Highlight</a></td>
      <td><code>
        I need to highlight these ==very important words==.
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#subscript">Subscript</a></td>
      <td><code>
        H~2~O
      </code></td>
    </tr>
    <tr>
      <td><a href="https://www.markdownguide.org/extended-syntax/#superscript">Superscript</a></td>
      <td><code>
        X^2^
      </code></td>
    </tr>
  </tbody>
</table>

## Basic Style

Below the basic style  [Markdown Guide](https://www.markdownguide.org/basic-syntax/) is 
restated as a verion local to this repository.

## Heading Best Practices

* Markdown applications don't agree on how to handle a missing space between the number signs (`#`) and the heading name. For compatibility, always put a space between the number signs and the heading name.

✅  Do this | ❌  Don't do this
-- | -- 
`# Here's a Heading` | `#Here's a Heading`

* Put blank lines before and after a heading for compatibility.

✅  Do this | ❌  Don't do this
-- | -- 
Try to put a blank line before...</br></br>`# Heading`</br></br>...and after a heading. | Without blank lines, this might not look correct.</br>`# Heading`</br>Don't do this!

## Paragraphs Best Practices

To create paragraphs, use a blank line to separate one or more lines of text.

Markdown | HTML | Rendered Output
-- | -- | --
`I really like using Markdown.`</br></br>`I think I'll use it to format all of my documents from now on.` | `<p>I really like using Markdown.</p>`</br></br>`<p>I think I'll use it to format all of my documents from now on.</p>` | I really like using Markdown.</br></br>I think I'll use it to format all of my documents from now on.
