        <div class="row">
          <!-- Listing 1 -->
          {% if listings %}
          <!-- for loop listings -->
          {% for listing in listings %}
          <div class="col-md-6 col-lg-4 mb-4">
            <div class="card listing-preview">
              {% comment %} fix {% endcomment %}
              <img
                class="card-img-top"
                src="{{ listing.photo_main.url}}"
                alt="{{listing.title | title}}"
              />
              <div class="card-img-overlay">
              </div>
              <div class="card-body">
                <div class="listing-heading text-center">
                  <h4 class="text-primary">{{listing.title | title}}</h4>
                  <p>
                    <i class="fas fa-map-marker text-secondary"></i> {{listing.district}}
                  </p>
                </div>
                <hr />
                <div class="row py-2 text-secondary">
                  <div class="col-6">
                    <i class="fas fa-th-large"></i> Fee : {{listing.service | apnumber | capfirst}}
                  </div>
                  <div class="col-6">
                    <i class="fas fa-dumbbell"></i> Treatment 
                  </div>
                </div>
                <div class="row py-2 text-secondary">
                  <div class="col-6">
                    <i class="fas fa-bed"></i> {{listing.rooms}}
                  </div>
                  <div class="col-6">
                    <i class="fas fa-bath"></i> Bathrooms
                  </div>
                </div>
                <hr />
                <div class="row py-2 text-secondary">
                  <div class="col-12"><i class="fas fa-user"></i> {{listing.doctor.name}}</div>
                </div>
                <div class="row text-secondary pb-2">
                  <div class="col-12">
                    <i class="fas fa-clock"></i> {{listing.list_date | timesince}}
                  </div>
                </div>
                <hr />
                <a href={% url 'listings:listing' listing.id %} class="btn btn-primary btn-block"
                  >More Info</a
                >
              </div>
            </div>
          </div>
          {% endfor %}
          <!-- end of for-loop -->
          {% else %}
          <div>
            <p>No Clinic Available.</p>
          </div>
          {% endif %}
        </div>
