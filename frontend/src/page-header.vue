<template>


  <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
    <div class="container-fluid">
     <img class="logo" src="@/assets/ServiceTrack.gif" alt="ServiceTrack">





      <div class="collapse navbar-collapse " id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">

           </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
               aria-expanded="false">
              Меню
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="/customers/">Заказчики</a></li>
              <li><a class="dropdown-item" href="/admin/">Админка</a></li>
              <li>
                <hr class="dropdown-divider">
              </li>
              <li><a class="dropdown-item" href="/admin/">Админка</a></li>
            </ul>
          </li>
        </ul>

        <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Поиск" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Поиск</button>
        </form>


      </div>
    </div>
  </nav>
</template>

<style>
.logo {
  height: 4em;
}


</style>