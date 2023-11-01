<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title')</title>
    @vite(['resources/js/app.js'])
</head>
<body>
    <nav class="navbar navbar-expand-lg bg-success ">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                <img src="https://static.vecteezy.com/system/resources/previews/013/649/594/non_2x/owl-education-illustration-on-a-background-premium-quality-symbols-icons-for-concept-and-graphic-design-vector.jpg" alt="Bootstrap" width="50">
            </a>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link active fs-5 {{request()->routeIs('apodoInicio')?'text-primary fw-bold':''}}" aria-current="page" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active fs-5 {{request()->routeIs('apodoFormulario')?'text-primary fw-bold':''}}" href="{{ route('apodoFormulario' )}}">Formulario</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link active fs-5 {{request()->routeIs('apodoRecuerdos')?'text-primary fw-bold':''}}" href="{{ route('apodoRecuerdos' )}}">Recuerdos</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    @yield('contenido')
    
    
</body>
</html>