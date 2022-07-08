# Architecture

The idea is to make building data entry as easy as dashboards using [Plotly Dash](https://dash.plotly.com) or [RStudio Shiny](https://shiny.rstudio.com) or [Streamlit](https://streamlit.io).

These frameworks have the same architecture.
They are [component web frameworks](https://stackoverflow.com/questions/4801891/difference-between-request-mvc-and-component-mvc) like [Apache Wicket](https://wicket.apache.org) or [Vaadin](https://vaadin.com/) in contrast to MVC web frameworks like Flask, Django or Spring MVC.
The former have state on the server, so it can be manipulated there and propagated to the browser via HTTP request (including AJAX) or Web Socket.
This decision greatly simplifies application development.

These days the frontend frameworks hype has slowed down and developers are starting to understand the benifit of coupling between the backend and frontend. Here are noticeable projects (this is an author opinion, `-` means not checked).

<table>
    <thead>
        <tr>
            <th>Library</th>
            <th>Language</th><th>Ajax</th><th>WS</th><th>Based on</th>
            <th>Comment</th>
        </tr>
    </thead>
    <tbody>
        <tr><th colspan="6">Backend ready</th></tr>
        <tr>
            <td><a href="https://github.com/phoenixframework/phoenix_live_view">Phoenix LiveView</a></td>
            <td>Elixir</td><td>-</td><td>Yes</td><td>-</td>
            <td>Inspirational</td>
        </tr>
        <tr>
            <td><a href="https://laravel-livewire.com">Laravel Livewire</a></td>
            <td>PHP (Laravel)</td><td>Yes</td><td>-</td><td>Components</td>
            <td>Inspirational</td>
        </tr>
        <tr>
            <td><a href="https://www.django-unicorn.com">Django Unicorn</a></td>
            <td>Python (Django)</td><td>Yes</td><td>No</td><td>Components</td>
            <td>
                Inspired by LiveView, Livewire and Hotwire.<br>
                Actively developed.
            </td>
        </tr>
        <tr>
            <td><a href="https://github.com/edelvalle/reactor">Reactor</a></td>
            <td>Python (Django)</td><td>-</td><td>Yes</td><td>Components</td>
            <td>
                Not actively developed.
            </td>
        </tr>
        <tr>
            <td><a href="https://github.com/mikeabrahamsen/Flask-Meld">Flask-Meld</a></td>
            <td>Python (Flask)</td><td>-</td><td>Yes</td><td>Components</td>
            <td>
                Inspired by LiveView, Livewire and Unicorn.<br>
                Uses AlpineJS as Livewire does.
                Not actively developed.
            </td>
        </tr>
        <tr>
            <td><a href="https://lona-web.org">Lona</a></td>
            <td>Python</td><td>-</td><td>-</td><td>Components</td>
            <td>-</td>
        </tr>
        <tr>
            <td><a href="https://justpy.io">JustPy</a></td>
            <td>Python</td><td>-</td><td>-</td><td>Components</td>
            <td>-</td>
        </tr>
        <tr>
            <td><a href="https://vaadin.com/">Vaadin</a></td>
            <td>Java</td><td>No</td><td>Yes</td><td>Components</td>
            <td>
                A mature production ready solution.
                The most close to Dash and Shiny.
                But using Java for prototyping is not fruitful.
            </td>
        </tr>
        <tr>
            <td><a href="https://wicket.apache.org/">Apache Wicket</a></td>
            <td>Java</td><td>Yes</td><td>No</td><td>Components</td>
            <td>
                Another mature solution.
                It's close to LiveView, Livewire and Unicorn.
                It's funny that Wicket didn't get as much attention as they are.
                But again Java dev speed is low for prototyping.
            </td>
        </tr>
    </tbody>
    <tbody>
        <tr><th colspan="6">Backend agnostic</th></tr>
        <tr>
            <td><a href="https://turbo.hotwired.dev">Hotwire Turbo</a></td>
            <td>Agnostic</td><td>Yes</td><td>Yes</td><td>Requests</td>
            <td></td>
        </tr>
        <tr>
            <td><a href="https://htmx.org">htmx</a></td>
            <td>Agnostic</td><td>Yes</td><td>Yes</td><td>Requests</td>
            <td></td>
        </tr>
        <tr>
            <td><a href="https://inertiajs.com">inertia.js</a></td>
            <td>Agnostic</td><td>Yes</td><td>No</td><td>Components</td>
            <td>
                Propagates props to frontend from the server using AJAX calls.
                Works with any frontend and backend framework.
            </td>
        </tr>
    </tbody>
</table>

As you see, there are a lot of solutions, so choose one and don't reinvent the wheel.

- A: **Flask-Meld** cause it is easy to use in quick apps with SQLAlchemy and Flask, though the project looks stale.
- B: **Hotwire or htmx** cause they are actively maintained and it would be easy to create small Flask extension for it, though it would require writing some component abstraction on top (or better implement it in **Flask-Meld**).
- ~~C: **Inertia.js** cause it is actively maintained and it would be easy to create small Flask extension for it and it has some component abstraction already, but it is not possible to use familiar backend templates.~~

Why not use Plotly Dash or Streamlit instead?
Because they are tightly coupled to the rest of the codebase for dashboarding and data analysis tasks.

Other ways:

- Plan D1: **Django Unicorn** with Django, though I'd prefer SQLAlchemy and Jinja or JS templates, but why not, after all it is great stack.
- Plan D2: Go Java with **Vaadin** 😂 and **Jooq ❤️**
- [Plan D12](https://www.youtube.com/watch?v=ttWQK5VXskA)
