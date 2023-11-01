

@extends('layouts.plantilla')

@section('titulo','Formulario')

@section('contenido')
<h1 class="display-1 text-center text-danger mt-5"> Formulario </h1>



<div class="container mt-5 col-md-6">
@if(session()->has('confirmacion'))
<div class="alert alert-success alert-dismissible fade show text-center" role="alert">
  <strong>{{session('confirmacion')}}</strong>
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
@endif
@if($errors->any())
@foreach($errors->all() as $error)
<div class="alert alert-success alert-dismissible fade show text-center" role="alert">
  <strong>{{$error}}</strong>
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
@endforeach
@endif



<div class="card">
  <div class="card-header text-primary fs-4 fw-semibold text-center">
    Formulario de Recuerdos
  </div>
  <div class="card-body">
  <form>

  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Titulo</label>
    <input type="text" class="form-control"  >
    <p class="text-danger fst-italic"> {{$errors->first('txtTitulo')}}</p>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Recuerdo</label>
    <input type="text" class="form-control" >
    {{$errors->first('txtRecuerdo')}}
  </div>


  </div>
  <div class="card-footer text-body-secondary">
  <div class="d-grid gap-2">
  <button type="submit" class="btn btn-outline-primary">Guardar Recuerdos</button>
  </div>
</form>
  </div>
</div>
</div>
@endsection


